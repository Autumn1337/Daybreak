from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import src.ai.newspaper as nr
from src.ai.newspaper import NewspaperRenderer
from src.models import ContentItem, SourceType


def _fresh_draw():
    img = Image.new("RGB", (2000, 200), (255, 255, 255))
    return ImageDraw.Draw(img)


def test_load_fonts_v2_returns_role_dict_with_latin_and_cjk():
    fonts = nr._load_fonts_v2()
    expected_roles = {
        "masthead", "masthead_sub", "masthead_info",
        "lead_kicker", "lead_title", "lead_deck", "lead_byline",
        "section_header", "item_title", "item_summary", "item_meta", "item_score",
        "footer",
    }
    assert set(fonts.keys()) == expected_roles
    for role, pair in fonts.items():
        assert isinstance(pair, tuple) and len(pair) == 2, role
        latin, cjk = pair
        assert isinstance(latin, (ImageFont.FreeTypeFont, ImageFont.ImageFont)), role
        assert isinstance(cjk, (ImageFont.FreeTypeFont, ImageFont.ImageFont)), role


def test_wrap_mixed_all_latin():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    lines = nr._wrap_mixed(draw, "The quick brown fox jumps over the lazy dog many times", role, max_width=300)
    assert len(lines) >= 2
    for line in lines:
        assert draw.textlength(line, font=role[0]) <= 320


def test_wrap_mixed_all_cjk_breaks_per_char():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    lines = nr._wrap_mixed(draw, "这是一段很长的中文测试文本需要被折行显示", role, max_width=150)
    assert len(lines) >= 2


def test_wrap_mixed_handles_mixed_zh_en():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    text = "Anthropic 发布 Claude Mythos Preview 系统卡片"
    lines = nr._wrap_mixed(draw, text, role, max_width=400)
    joined = "".join(l.rstrip() for l in lines)
    # char count preserved (whitespace may be trimmed at line boundaries but chars present)
    for ch in text.replace(" ", ""):
        assert ch in joined


def test_measure_run_empty_returns_zero():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    assert nr._measure_run(draw, "", role) == 0


def test_measure_run_with_tracking():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    w0 = nr._measure_run(draw, "ABC", role, tracking=0)
    w1 = nr._measure_run(draw, "ABC", role, tracking=10)
    # 3 chars = 2 gaps
    assert w1 == w0 + 20


def test_line_height_role_positive():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    assert nr._line_height_role(draw, role) > 0


def test_measure_wrapped_returns_lines_times_line_height():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    h, n = nr._measure_wrapped(draw, "word " * 40, role, max_width=200, line_gap=10)
    assert n >= 2
    lh = nr._line_height_role(draw, role)
    assert h == n * lh + (n - 1) * 10


def test_measure_wrapped_max_lines_truncates():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    _h1, n_all = nr._measure_wrapped(draw, "word " * 40, role, max_width=200, line_gap=0)
    _h2, n_cap = nr._measure_wrapped(draw, "word " * 40, role, max_width=200, line_gap=0, max_lines=2)
    assert n_all > 2
    assert n_cap == 2


def test_draw_wrapped_returns_y_after_text():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["item_summary"]
    end_y = nr._draw_wrapped(draw, 10, 20, "Hello world this is a long line", role,
                             color=(0, 0, 0), max_width=150, line_gap=4)
    assert end_y > 20


def test_draw_centered_run_smoke():
    draw = _fresh_draw()
    role = nr._load_fonts_v2()["lead_kicker"]
    nr._draw_centered_run(draw, cx=500, y=50, text="AI / ML", role=role,
                          color=(0, 0, 0), tracking=4)


def test_compute_item_positions_row_major():
    r = NewspaperRenderer()
    draw = _fresh_draw()
    items = [{
        "title": f"Item {i}",
        "summary": f"Summary for item {i}. Short.",
        "score": 8.0 - i * 0.1,
        "category": "AI/ML",
        "source": f"src{i} · Apr 24",
    } for i in range(5)]
    positions = r._compute_item_positions(draw, items, start_y=100)
    assert len(positions) == 5
    assert positions[0][0] == nr.MARGIN_X
    assert positions[1][0] == nr.MARGIN_X + nr.COL_W + nr.COL_GAP
    assert positions[2][0] == nr.MARGIN_X + 2 * (nr.COL_W + nr.COL_GAP)
    assert positions[0][1] == positions[1][1] == positions[2][1] == 100
    assert positions[3][0] == nr.MARGIN_X
    assert positions[3][1] > 100
    assert positions[3][1] == positions[4][1]


def test_newspaper_renderer_multi_category_end_to_end(tmp_path):
    cats = ["AI/ML", "AI/ML", "AI/ML", "Security", "Security", "Industry"]
    items = []
    for i, cat in enumerate(cats):
        it = ContentItem(
            id=f"rss:test:{i}",
            source_type=SourceType.RSS,
            title=f"Item {i} · 中英混排测试 {cat}",
            url=f"https://example.com/item-{i}",
            content="content",
            author="tester",
            published_at=datetime.now(timezone.utc),
        )
        it.ai_score = 9.0 - i * 0.3
        it.ai_summary = f"摘要 {i}：这是一段中英混排的测试文本，用于验证 CJK 和 Latin 字符的 fallback 行为是否正确。Lorem ipsum dolor."
        it.ai_category = cat
        items.append(it)
    renderer = NewspaperRenderer()
    png = renderer.render(items, "2026-04-24", total_fetched=len(items), language="zh")
    assert png.startswith(b"\x89PNG\r\n\x1a\n")
    assert len(png) > 10_000


def test_newspaper_renderer_falls_back_when_truetype_is_unavailable(monkeypatch) -> None:
    monkeypatch.setattr("src.ai.newspaper._font_path_candidates", lambda *names: [])

    item = ContentItem(
        id="rss:test:1",
        source_type=SourceType.RSS,
        title="Fallback font smoke test",
        url="https://example.com/item-1",
        content="content",
        author="tester",
        published_at=datetime.now(timezone.utc),
    )
    item.ai_score = 8.5
    item.ai_summary = "Renderer should still produce a PNG when custom fonts are missing."
    item.ai_category = "AI/ML"

    renderer = NewspaperRenderer()
    image = renderer.render([item], "2026-04-08", total_fetched=1, language="en")

    assert image.startswith(b"\x89PNG\r\n\x1a\n")
