"""Newspaper-style image renderer for Daybreak daily digest.

Renders ContentItem lists into a multi-column newspaper PNG using Pillow.
"""

import io
import os
import re
from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont

from ..models import ContentItem
from .summarizer import CATEGORY_ORDER

# ── Page geometry ────────────────────────────────────
SCALE = 3
PAGE_W = 1200 * SCALE
MARGIN_X = 50 * SCALE
MARGIN_Y = 40 * SCALE
COL_GAP = 28 * SCALE
NUM_COLS = 3
CONTENT_W = PAGE_W - 2 * MARGIN_X
COL_W = (CONTENT_W - (NUM_COLS - 1) * COL_GAP) // NUM_COLS

# ── Colors ───────────────────────────────────────────
C_BG = (253, 249, 240)
C_TEXT = (28, 28, 28)
C_RULE = (61, 49, 38)
C_RULE_LIGHT = (190, 180, 165)
C_ACCENT = (139, 26, 26)
C_MUTED = (120, 120, 120)
C_CAT_BG = (61, 49, 38)
C_CAT_TEXT = (253, 249, 240)

# ── Pangu spacing ────────────────────────────────────
_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


# ── Font helpers ─────────────────────────────────────
FONTS_DIR = os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts")


def _fp(name):
    return os.path.join(FONTS_DIR, name)


def _font_path_candidates(*names: str):
    search_roots = [
        Path(FONTS_DIR),
        Path("/usr/share/fonts"),
        Path("/usr/local/share/fonts"),
        Path.home() / ".fonts",
        Path("/System/Library/Fonts"),
        Path("/Library/Fonts"),
    ]
    seen: set[str] = set()

    for name in names:
        candidate = Path(name)
        if candidate.is_absolute():
            candidate_str = str(candidate)
            if candidate_str not in seen:
                seen.add(candidate_str)
                yield candidate
            continue

        for root in search_roots:
            path = root / name
            path_str = str(path)
            if path_str in seen:
                continue
            seen.add(path_str)
            yield path


def _load_font(size: int, *names: str):
    for path in _font_path_candidates(*names):
        if not path.exists():
            continue
        try:
            return ImageFont.truetype(str(path), size)
        except OSError:
            continue
    return ImageFont.load_default()


def _load_fonts():
    S = SCALE
    f = {
        "masthead": _load_font(
            56 * S,
            "timesbd.ttf",
            "georgiab.ttf",
            "truetype/dejavu/DejaVuSerif-Bold.ttf",
            "truetype/liberation2/LiberationSerif-Bold.ttf",
        ),
        "subtitle": _load_font(
            16 * S,
            "NotoSerifSC-VF.ttf",
            "msyh.ttc",
            "simsun.ttc",
            "opentype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSerif.ttf",
            "truetype/liberation2/LiberationSerif-Regular.ttf",
        ),
        "date": _load_font(
            14 * S,
            "NotoSansSC-VF.ttf",
            "msyh.ttc",
            "simhei.ttf",
            "opentype/noto/NotoSansCJK-Regular.ttc",
            "truetype/noto/NotoSansCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSans.ttf",
            "truetype/liberation2/LiberationSans-Regular.ttf",
        ),
        "lead_title": _load_font(
            26 * S,
            "NotoSerifSC-VF.ttf",
            "msyh.ttc",
            "simsun.ttc",
            "opentype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSerif-Bold.ttf",
            "truetype/liberation2/LiberationSerif-Bold.ttf",
        ),
        "lead_body": _load_font(
            15 * S,
            "NotoSansSC-VF.ttf",
            "msyh.ttc",
            "simhei.ttf",
            "opentype/noto/NotoSansCJK-Regular.ttc",
            "truetype/noto/NotoSansCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSans.ttf",
            "truetype/liberation2/LiberationSans-Regular.ttf",
        ),
        "item_title": _load_font(
            16 * S,
            "NotoSerifSC-VF.ttf",
            "msyh.ttc",
            "simsun.ttc",
            "opentype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/noto/NotoSerifCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSerif-Bold.ttf",
            "truetype/liberation2/LiberationSerif-Bold.ttf",
        ),
        "body": _load_font(
            13 * S,
            "NotoSansSC-VF.ttf",
            "msyh.ttc",
            "simhei.ttf",
            "opentype/noto/NotoSansCJK-Regular.ttc",
            "truetype/noto/NotoSansCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSans.ttf",
            "truetype/liberation2/LiberationSans-Regular.ttf",
        ),
        "score": _load_font(
            11 * S,
            "georgiab.ttf",
            "timesbd.ttf",
            "truetype/dejavu/DejaVuSerif-Bold.ttf",
            "truetype/liberation2/LiberationSerif-Bold.ttf",
        ),
        "source": _load_font(
            11 * S,
            "NotoSansSC-VF.ttf",
            "msyh.ttc",
            "simhei.ttf",
            "opentype/noto/NotoSansCJK-Regular.ttc",
            "truetype/noto/NotoSansCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSans.ttf",
            "truetype/liberation2/LiberationSans-Regular.ttf",
        ),
        "category": _load_font(
            13 * S,
            "simhei.ttf",
            "NotoSansSC-VF.ttf",
            "msyh.ttc",
            "opentype/noto/NotoSansCJK-Regular.ttc",
            "truetype/noto/NotoSansCJK-Regular.ttc",
            "truetype/dejavu/DejaVuSans-Bold.ttf",
            "truetype/liberation2/LiberationSans-Bold.ttf",
        ),
        "footer": _load_font(
            11 * S,
            "georgiai.ttf",
            "timesi.ttf",
            "truetype/dejavu/DejaVuSerif-Italic.ttf",
            "truetype/liberation2/LiberationSerif-Italic.ttf",
            "truetype/dejavu/DejaVuSerif.ttf",
        ),
    }
    for key in ("lead_title", "item_title"):
        try:
            f[key].set_variation_by_axes([700])
        except Exception:
            pass
    return f


# ── Text utilities ───────────────────────────────────
def _is_cjk(ch):
    cp = ord(ch)
    return (
        0x4E00 <= cp <= 0x9FFF
        or 0x3400 <= cp <= 0x4DBF
        or 0x2E80 <= cp <= 0x2EFF
        or 0xF900 <= cp <= 0xFAFF
        or 0xFE30 <= cp <= 0xFE4F
        or 0x3000 <= cp <= 0x303F
        or 0xFF00 <= cp <= 0xFFEF
    )


def _wrap_text(draw, text, font, max_width):
    if not text:
        return []
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        current = ""
        for ch in paragraph:
            test = current + ch
            if draw.textlength(test, font=font) <= max_width:
                current = test
            else:
                if not current:
                    lines.append(ch)
                    continue
                if _is_cjk(ch):
                    lines.append(current)
                    current = ch
                elif ch == " ":
                    lines.append(current)
                    current = ""
                else:
                    last_space = current.rfind(" ")
                    last_cjk = -1
                    for j in range(len(current) - 1, -1, -1):
                        if _is_cjk(current[j]):
                            last_cjk = j
                            break
                    bp = max(last_space, last_cjk)
                    if bp > 0:
                        lines.append(current[: bp + 1].rstrip())
                        current = current[bp + 1 :].lstrip() + ch
                    else:
                        lines.append(current)
                        current = ch
        if current:
            lines.append(current)
    return lines


def _line_height(draw, font):
    return draw.textbbox((0, 0), "Ayg你好", font=font)[3] - draw.textbbox((0, 0), "Ayg你好", font=font)[1]


def _draw_text_block(draw, text, x, y, font, color, max_width, spacing=4, max_lines=None):
    lines = _wrap_text(draw, text, font, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines[-1]:
            while lines[-1] and draw.textlength(lines[-1] + "…", font=font) > max_width:
                lines[-1] = lines[-1][:-1]
            lines[-1] += "…"
    lh = _line_height(draw, font)
    for line in lines:
        draw.text((x, y), line, fill=color, font=font)
        y += lh + spacing
    return y


def _measure_text_block(draw, text, font, max_width, spacing=4, max_lines=None):
    lines = _wrap_text(draw, text, font, max_width)
    if max_lines:
        lines = lines[:max_lines]
    if not lines:
        return 0
    lh = _line_height(draw, font)
    return len(lines) * (lh + spacing)


# ── Drawing helpers ──────────────────────────────────
def _hline(draw, x1, x2, y, color=C_RULE, width=1):
    draw.line([(x1, y), (x2, y)], fill=color, width=width)


def _double_rule(draw, x1, x2, y, color=C_RULE):
    draw.line([(x1, y), (x2, y)], fill=color, width=2 * SCALE)
    draw.line([(x1, y + 5 * SCALE), (x2, y + 5 * SCALE)], fill=color, width=SCALE)
    return y + 6 * SCALE


def _ornament(draw, cx, y, color=C_RULE):
    r = 4 * SCALE
    draw.polygon([(cx, y - r), (cx + r, y), (cx, y + r), (cx - r, y)], fill=color)


# ── Data extraction ──────────────────────────────────
def _item_render_data(item: ContentItem, language: str = "zh") -> dict:
    """Extract rendering data from a ContentItem."""
    title = item.metadata.get(f"title_{language}") or item.title
    summary = (
        item.metadata.get(f"detailed_summary_{language}")
        or item.metadata.get("detailed_summary")
        or item.ai_summary
        or ""
    )
    if language == "zh":
        title = _pangu(str(title))
        summary = _pangu(summary)

    source_parts = [item.source_type.value]
    if item.metadata.get("subreddit"):
        source_parts.append(f"r/{item.metadata['subreddit']}")
    elif item.metadata.get("feed_name"):
        source_parts.append(item.metadata["feed_name"])
    if item.published_at:
        day = item.published_at.strftime("%d").lstrip("0")
        source_parts.append(item.published_at.strftime(f"%b {day}"))

    return {
        "title": str(title),
        "summary": summary,
        "score": item.ai_score or 0,
        "category": item.ai_category or "Other",
        "source": " · ".join(source_parts),
    }


# ── Renderer ─────────────────────────────────────────
class NewspaperRenderer:
    def __init__(self):
        self.fonts = _load_fonts()

    def render(
        self,
        items: List[ContentItem],
        date_str: str,
        total_fetched: int,
        language: str = "zh",
    ) -> bytes:
        """Render items as a newspaper-style PNG image.

        Returns PNG bytes.
        """
        # Sort by category order, then score descending
        cat_rank = {c: i for i, c in enumerate(CATEGORY_ORDER)}
        sorted_items = sorted(
            items,
            key=lambda x: (cat_rank.get(x.ai_category or "Other", 99), -(x.ai_score or 0)),
        )
        render_data = [_item_render_data(it, language) for it in sorted_items]

        img = Image.new("RGB", (PAGE_W, 8000 * SCALE), C_BG)
        draw = ImageDraw.Draw(img)

        y = MARGIN_Y
        y = self._draw_masthead(draw, y, date_str, total_fetched, len(items), language)

        if render_data:
            y = self._draw_lead(draw, y, render_data[0])

        if len(render_data) > 1:
            y = self._draw_columns(draw, y, render_data[1:])

        y = self._draw_footer(draw, y)
        img = img.crop((0, 0, PAGE_W, y + MARGIN_Y))

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()

    def _draw_masthead(self, draw, y, date_str, total, selected, language):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        y = _double_rule(draw, x1, x2, y)
        y += 20 * S

        title = "D  A  Y  B  R  E  A  K"
        tw = draw.textlength(title, font=self.fonts["masthead"])
        draw.text(((PAGE_W - tw) / 2, y), title, fill=C_TEXT, font=self.fonts["masthead"])
        y += _line_height(draw, self.fonts["masthead"]) + 8 * S

        sub = "每 日 速 递" if language == "zh" else "Daily Digest"
        sw = draw.textlength(sub, font=self.fonts["subtitle"])
        draw.text(((PAGE_W - sw) / 2, y), sub, fill=C_MUTED, font=self.fonts["subtitle"])
        y += _line_height(draw, self.fonts["subtitle"]) + 12 * S

        labels = {
            "zh": f"{date_str}  ·  从 {total} 条内容中精选 {selected} 条重要资讯",
            "en": f"{date_str}  ·  {selected} important items selected from {total}",
        }
        info = labels.get(language, labels["en"])
        iw = draw.textlength(info, font=self.fonts["date"])
        draw.text(((PAGE_W - iw) / 2, y), info, fill=C_MUTED, font=self.fonts["date"])
        y += _line_height(draw, self.fonts["date"]) + 16 * S

        half = 120 * S
        cx = PAGE_W // 2
        _hline(draw, cx - half - 20 * S, cx - 12 * S, y + S, C_RULE_LIGHT)
        _ornament(draw, cx, y + S, C_RULE)
        _hline(draw, cx + 12 * S, cx + half + 20 * S, y + S, C_RULE_LIGHT)
        y += 16 * S

        y = _double_rule(draw, x1, x2, y)
        y += 12 * S
        return y

    def _draw_lead(self, draw, y, item):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X

        cat = item["category"]
        cw = draw.textlength(f"  {cat}  ", font=self.fonts["category"])
        ch = _line_height(draw, self.fonts["category"]) + 8 * S
        draw.rectangle([(x1, y), (x1 + cw, y + ch)], fill=C_CAT_BG)
        draw.text((x1 + 6 * S, y + 4 * S), cat, fill=C_CAT_TEXT, font=self.fonts["category"])

        score_text = f"★ {item['score']:.1f}"
        stw = draw.textlength(score_text, font=self.fonts["score"])
        draw.text((x2 - stw, y + 4 * S), score_text, fill=C_ACCENT, font=self.fonts["score"])
        y += ch + 10 * S

        y = _draw_text_block(draw, item["title"], x1, y, self.fonts["lead_title"], C_TEXT, CONTENT_W, spacing=3 * S)
        y += 6 * S
        y = _draw_text_block(draw, item["summary"], x1, y, self.fonts["lead_body"], C_TEXT, CONTENT_W, spacing=5 * S, max_lines=4)
        y += 4 * S
        draw.text((x1, y), item["source"], fill=C_MUTED, font=self.fonts["source"])
        y += _line_height(draw, self.fonts["source"]) + 14 * S

        _hline(draw, x1, x2, y, C_RULE)
        y += 20 * S
        return y

    def _draw_columns(self, draw, start_y, items):
        x1 = MARGIN_X

        item_heights = [self._measure_item(draw, it) for it in items]
        cat_h = _line_height(draw, self.fonts["category"]) + 18 * SCALE

        cols = [[] for _ in range(NUM_COLS)]
        col_h = [0.0] * NUM_COLS
        last_cat_per_col = [None] * NUM_COLS

        for i, item in enumerate(items):
            target = col_h.index(min(col_h))
            if item["category"] != last_cat_per_col[target]:
                cols[target].append(("cat", item["category"]))
                col_h[target] += cat_h
                last_cat_per_col[target] = item["category"]
            cols[target].append(("item", item))
            col_h[target] += item_heights[i]

        max_col_h = max(col_h) if col_h else 0

        for ci, entries in enumerate(cols):
            cx = x1 + ci * (COL_W + COL_GAP)
            cy = start_y
            for etype, data in entries:
                if etype == "cat":
                    cy = self._draw_category_header(draw, cy, data, cx)
                else:
                    cy = self._draw_item(draw, cy, data, cx)

        for ci in range(1, NUM_COLS):
            rx = x1 + ci * (COL_W + COL_GAP) - COL_GAP // 2
            draw.line([(rx, start_y), (rx, start_y + max_col_h)], fill=C_RULE_LIGHT, width=1)

        return start_y + max_col_h + 10 * SCALE

    def _measure_item(self, draw, item):
        S = SCALE
        h = _measure_text_block(draw, item["title"], self.fonts["item_title"], COL_W, spacing=2 * S)
        h += 6 * S
        h += _measure_text_block(draw, item["summary"], self.fonts["body"], COL_W, spacing=3 * S, max_lines=3)
        h += 4 * S
        h += _line_height(draw, self.fonts["source"]) + 4 * S
        h += 16 * S
        return h

    def _draw_category_header(self, draw, y, category, x):
        S = SCALE
        cw = draw.textlength(f"  {category}  ", font=self.fonts["category"])
        ch = _line_height(draw, self.fonts["category"]) + 8 * S
        draw.rectangle([(x, y), (x + cw, y + ch)], fill=C_CAT_BG)
        draw.text((x + 6 * S, y + 4 * S), category, fill=C_CAT_TEXT, font=self.fonts["category"])
        y += ch + 10 * S
        return y

    def _draw_item(self, draw, y, item, x):
        S = SCALE
        y = _draw_text_block(draw, item["title"], x, y, self.fonts["item_title"], C_TEXT, COL_W, spacing=2 * S)
        y += 4 * S
        y = _draw_text_block(draw, item["summary"], x, y, self.fonts["body"], C_TEXT, COL_W, spacing=3 * S, max_lines=3)
        y += 3 * S
        draw.text((x, y), item["source"], fill=C_MUTED, font=self.fonts["source"])
        score_text = f"★ {item['score']:.1f}"
        stw = draw.textlength(score_text, font=self.fonts["score"])
        draw.text((x + COL_W - stw, y), score_text, fill=C_ACCENT, font=self.fonts["score"])
        y += _line_height(draw, self.fonts["source"]) + 8 * S
        _hline(draw, x, x + COL_W, y, C_RULE_LIGHT)
        y += 10 * S
        return y

    def _draw_footer(self, draw, y):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        y += 4 * S
        _double_rule(draw, x1, x2, y)
        y += 14 * S
        footer = "Daybreak  ·  AI-Powered Tech Intelligence  ·  github.com/Autumn1337/Daybreak"
        fw = draw.textlength(footer, font=self.fonts["footer"])
        draw.text(((PAGE_W - fw) / 2, y), footer, fill=C_MUTED, font=self.fonts["footer"])
        y += _line_height(draw, self.fonts["footer"]) + 4 * S
        return y
