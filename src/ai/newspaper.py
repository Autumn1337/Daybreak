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
from .summarizer import CATEGORY_ORDER, _normalize_category

# ── Page geometry ────────────────────────────────────
SCALE = 5
PAGE_W = 1200 * SCALE
MARGIN_X = 72 * SCALE
MARGIN_Y = 56 * SCALE
COL_GAP = 40 * SCALE
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


# ── Bundled fonts + role-based loading ───────────────
FONT_DIR = Path(__file__).resolve().parents[2] / "data" / "fonts"


def _load_static(filename: str, size: int):
    bundled = FONT_DIR / filename
    if bundled.exists():
        try:
            return ImageFont.truetype(str(bundled), size)
        except OSError:
            pass
    for path in _font_path_candidates(filename):
        if not path.exists():
            continue
        try:
            return ImageFont.truetype(str(path), size)
        except OSError:
            continue
    return ImageFont.load_default()


def _load_fonts_v2() -> dict:
    """Return role → (latin_font, cjk_font) pairs for the redesigned layout."""
    S = SCALE

    def pair(latin_file: str, latin_axes, cjk_weight: int, size_pt: int):
        latin = _load_static(latin_file, size_pt * S)
        if latin_axes is not None:
            try:
                latin.set_variation_by_axes(list(latin_axes))
            except Exception:
                pass
        cjk = _load_static("NotoSerifSC-VF.ttf", size_pt * S)
        try:
            cjk.set_variation_by_axes([cjk_weight])
        except Exception:
            pass
        return (latin, cjk)

    return {
        "masthead":       pair("SourceSerif4-Black.ttf",   None,      900, 60),
        "masthead_sub":   pair("Inter-VF.ttf",             [14, 600], 500, 15),
        "masthead_info":  pair("SourceSerif4-Regular.ttf", None,      400, 13),
        "lead_kicker":    pair("Inter-VF.ttf",             [14, 700], 700, 12),
        "lead_title":     pair("SourceSerif4-Black.ttf",   None,      900, 34),
        "lead_deck":      pair("SourceSerif4-It.ttf",      None,      400, 18),
        "lead_byline":    pair("Inter-Italic-VF.ttf",      [14, 400], 400, 12),
        "section_header": pair("SourceSerif4-Bold.ttf",    None,      700, 17),
        "item_title":     pair("SourceSerif4-Bold.ttf",    None,      700, 18),
        "item_summary":   pair("SourceSerif4-Regular.ttf", None,      400, 15),
        "item_meta":      pair("SourceSerif4-It.ttf",      None,      400, 12),
        "item_score":     pair("SourceSerif4-Bold.ttf",    None,      700, 13),
        "footer":         pair("SourceSerif4-It.ttf",      None,      400, 12),
    }


# ── V2: Mixed-script text primitives ─────────────────────
def _measure_run(draw, text: str, role: tuple, tracking: int = 0) -> float:
    if not text:
        return 0
    latin, cjk = role
    w = 0.0
    for ch in text:
        font = cjk if _is_cjk(ch) else latin
        w += draw.textlength(ch, font=font)
        w += tracking
    return w - tracking


def _draw_run(draw, x: float, y: float, text: str, role: tuple, color, tracking: int = 0) -> float:
    latin, cjk = role
    for ch in text:
        font = cjk if _is_cjk(ch) else latin
        draw.text((x, y), ch, fill=color, font=font)
        x += draw.textlength(ch, font=font) + tracking
    return x - (tracking if text else 0)


def _line_height_role(draw, role: tuple) -> int:
    latin, cjk = role
    bl = draw.textbbox((0, 0), "Ayg", font=latin)
    bc = draw.textbbox((0, 0), "你好", font=cjk)
    return max(bl[3] - bl[1], bc[3] - bc[1])


def _wrap_mixed(draw, text: str, role: tuple, max_width: float, tracking: int = 0) -> list:
    if not text:
        return []
    lines: list = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        current = ""
        for ch in paragraph:
            test = current + ch
            if _measure_run(draw, test, role, tracking) <= max_width:
                current = test
                continue
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


def _measure_wrapped(draw, text: str, role: tuple, max_width: float,
                     line_gap: int = 0, max_lines=None, tracking: int = 0) -> tuple:
    lines = _wrap_mixed(draw, text, role, max_width, tracking)
    if max_lines is not None:
        lines = lines[:max_lines]
    n = len(lines)
    if n == 0:
        return (0, 0)
    lh = _line_height_role(draw, role)
    return (n * lh + (n - 1) * line_gap, n)


def _draw_wrapped(draw, x: float, y: float, text: str, role: tuple, color,
                  max_width: float, line_gap: int = 0, max_lines=None,
                  tracking: int = 0) -> float:
    lines = _wrap_mixed(draw, text, role, max_width, tracking)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines[-1]:
            while lines[-1] and _measure_run(draw, lines[-1] + "…", role, tracking) > max_width:
                lines[-1] = lines[-1][:-1]
            lines[-1] = lines[-1] + "…"
    lh = _line_height_role(draw, role)
    for i, line in enumerate(lines):
        _draw_run(draw, x, y, line, role, color, tracking)
        y += lh
        if i < len(lines) - 1:
            y += line_gap
    return y


def _draw_centered_run(draw, cx: float, y: float, text: str, role: tuple,
                       color, tracking: int = 0) -> None:
    w = _measure_run(draw, text, role, tracking)
    _draw_run(draw, cx - w / 2, y, text, role, color, tracking)


def _draw_wrapped_centered(draw, cx: float, y: float, text: str, role: tuple,
                           color, max_width: float, line_gap: int = 0,
                           max_lines=None, tracking: int = 0) -> float:
    lines = _wrap_mixed(draw, text, role, max_width, tracking)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines[-1]:
            while lines[-1] and _measure_run(draw, lines[-1] + "…", role, tracking) > max_width:
                lines[-1] = lines[-1][:-1]
            lines[-1] = lines[-1] + "…"
    lh = _line_height_role(draw, role)
    for i, line in enumerate(lines):
        w = _measure_run(draw, line, role, tracking)
        _draw_run(draw, cx - w / 2, y, line, role, color, tracking)
        y += lh
        if i < len(lines) - 1:
            y += line_gap
    return y


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
        "category": _normalize_category(item.ai_category),
        "source": " · ".join(source_parts),
    }


# ── Renderer ─────────────────────────────────────────
class NewspaperRenderer:
    def __init__(self):
        self.fonts_v2 = _load_fonts_v2()

    def render(
        self,
        items: List[ContentItem],
        date_str: str,
        total_fetched: int,
        language: str = "zh",
    ) -> bytes:
        cat_rank = {c: i for i, c in enumerate(CATEGORY_ORDER)}
        sorted_items = sorted(
            items,
            key=lambda x: (cat_rank.get(_normalize_category(x.ai_category), 99), -(x.ai_score or 0)),
        )
        render_data = [_item_render_data(it, language) for it in sorted_items]

        # Pass 1: measure final height on a tiny throwaway canvas.
        # Pillow silently clips out-of-bounds draw ops, so y returns are still correct.
        tmp_img = Image.new("RGB", (PAGE_W, 16), C_BG)
        tmp_draw = ImageDraw.Draw(tmp_img)
        measured_y = self._run_layout(tmp_draw, render_data, date_str, total_fetched,
                                      len(items), language)
        final_h = measured_y + MARGIN_Y

        # Pass 2: allocate exact canvas and render for real.
        Image.MAX_IMAGE_PIXELS = max(
            Image.MAX_IMAGE_PIXELS or 0,
            PAGE_W * final_h + 1,
        )
        img = Image.new("RGB", (PAGE_W, final_h), C_BG)
        draw = ImageDraw.Draw(img)
        self._run_layout(draw, render_data, date_str, total_fetched, len(items), language)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()

    def _run_layout(self, draw, render_data, date_str, total_fetched, total_items, language):
        y = MARGIN_Y
        y = self._draw_masthead_v2(draw, y, date_str, total_fetched, total_items, language)
        if render_data:
            y = self._draw_lead_v2(draw, y, render_data[0])
        if len(render_data) > 1:
            groups = self._group_by_category(render_data[1:])
            for cat, group_items in groups:
                y = self._draw_section_header(draw, y, cat)
                y = self._draw_section_items(draw, y, group_items)
        y = self._draw_footer_v2(draw, y)
        return y

    # ── Masthead ──────────────────────────────────────
    def _draw_masthead_v2(self, draw, y, date_str, total, selected, language):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        cx = PAGE_W // 2

        y = _double_rule(draw, x1, x2, y)
        y += 22 * S

        title_role = self.fonts_v2["masthead"]
        _draw_centered_run(draw, cx, y, "DAYBREAK", title_role, C_TEXT, tracking=12 * S)
        y += _line_height_role(draw, title_role) + 10 * S

        sub_role = self.fonts_v2["masthead_sub"]
        sub_text = "DAILY DIGEST" if language != "zh" else "每 日 速 递"
        _draw_centered_run(draw, cx, y, sub_text, sub_role, C_MUTED, tracking=4 * S)
        y += _line_height_role(draw, sub_role) + 12 * S

        info_role = self.fonts_v2["masthead_info"]
        labels = {
            "zh": f"{date_str}  ·  从 {total} 条内容中精选 {selected} 条重要资讯",
            "en": f"{date_str}  ·  {selected} important items selected from {total}",
        }
        info = labels.get(language, labels["en"])
        _draw_centered_run(draw, cx, y, info, info_role, C_MUTED)
        y += _line_height_role(draw, info_role) + 18 * S

        half = 140 * S
        _hline(draw, cx - half - 20 * S, cx - 12 * S, y + S, C_RULE_LIGHT)
        _ornament(draw, cx, y + S, C_RULE)
        _hline(draw, cx + 12 * S, cx + half + 20 * S, y + S, C_RULE_LIGHT)
        y += 18 * S

        y = _double_rule(draw, x1, x2, y)
        y += 14 * S
        return y

    # ── Lead (NYT front page) ────────────────────────
    def _draw_lead_v2(self, draw, y, item):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        cx = PAGE_W // 2

        y += 12 * S

        kicker_role = self.fonts_v2["lead_kicker"]
        kicker = f"{item['category']}  ·  ★ {item['score']:.1f}"
        _draw_centered_run(draw, cx, y, kicker.upper(), kicker_role, C_ACCENT, tracking=4 * S)
        y += _line_height_role(draw, kicker_role) + 12 * S

        title_role = self.fonts_v2["lead_title"]
        y = _draw_wrapped_centered(
            draw, cx, y, item["title"], title_role, C_TEXT,
            max_width=CONTENT_W, line_gap=6 * S, max_lines=3,
        )
        y += 16 * S

        deck_role = self.fonts_v2["lead_deck"]
        deck_w = int(CONTENT_W * 0.82)
        y = _draw_wrapped_centered(
            draw, cx, y, item["summary"], deck_role, C_TEXT,
            max_width=deck_w, line_gap=7 * S, max_lines=3,
        )
        y += 14 * S

        byline_role = self.fonts_v2["lead_byline"]
        _draw_centered_run(draw, cx, y, item["source"].upper(), byline_role, C_MUTED, tracking=2 * S)
        y += _line_height_role(draw, byline_role) + 20 * S

        _hline(draw, x1, x2, y, C_RULE)
        _ornament(draw, cx, y, C_RULE)
        y += 14 * S
        return y

    # ── Section header (α style) ─────────────────────
    def _draw_section_header(self, draw, y, label: str):
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        cx = PAGE_W // 2

        y += 28 * S

        role = self.fonts_v2["section_header"]
        tracking = 5 * S
        caps_text = label.upper()
        w = _measure_run(draw, caps_text, role, tracking)
        lh = _line_height_role(draw, role)

        cy_text = y + lh // 2  # vertical center of text line — the rule sits here
        ornament_r = 4 * S
        pad = 14 * S

        text_left = cx - w / 2
        text_right = cx + w / 2
        diamond_left_cx = text_left - pad - ornament_r
        diamond_right_cx = text_right + pad + ornament_r

        _hline(draw, x1, int(diamond_left_cx - ornament_r), cy_text, C_RULE)
        _ornament(draw, int(diamond_left_cx), cy_text, C_RULE)
        _draw_run(draw, text_left, y, caps_text, role, C_TEXT, tracking)
        _ornament(draw, int(diamond_right_cx), cy_text, C_RULE)
        _hline(draw, int(diamond_right_cx + ornament_r), x2, cy_text, C_RULE)

        y += lh + 18 * S
        return y

    # ── Item card ────────────────────────────────────
    def _measure_item_v2(self, draw, item: dict) -> int:
        S = SCALE
        inner_w = COL_W - 14 * S  # padding past the red rule
        h = 0
        th, _ = _measure_wrapped(draw, item["title"], self.fonts_v2["item_title"],
                                 max_width=inner_w, line_gap=3 * S, max_lines=3)
        h += th
        h += 9 * S
        sh, _ = _measure_wrapped(draw, item["summary"], self.fonts_v2["item_summary"],
                                 max_width=inner_w, line_gap=6 * S, max_lines=3)
        h += sh
        h += 11 * S
        h += _line_height_role(draw, self.fonts_v2["item_meta"])
        return h

    def _draw_item_v2(self, draw, x: int, y: int, item: dict) -> int:
        S = SCALE
        inner_x = x + 14 * S
        inner_w = COL_W - 14 * S
        start_y = y

        end_y = _draw_wrapped(draw, inner_x, y, item["title"], self.fonts_v2["item_title"],
                              C_TEXT, max_width=inner_w, line_gap=3 * S, max_lines=3)
        y = end_y + 9 * S

        end_y = _draw_wrapped(draw, inner_x, y, item["summary"], self.fonts_v2["item_summary"],
                              C_TEXT, max_width=inner_w, line_gap=6 * S, max_lines=3)
        y = end_y + 11 * S

        meta_role = self.fonts_v2["item_meta"]
        score_role = self.fonts_v2["item_score"]
        lh_meta = _line_height_role(draw, meta_role)
        _draw_run(draw, inner_x, y, item["source"], meta_role, C_MUTED)
        score_text = f"★ {item['score']:.1f}"
        sw = _measure_run(draw, score_text, score_role)
        _draw_run(draw, x + COL_W - sw, y, score_text, score_role, C_ACCENT)
        y += lh_meta

        card_h = y - start_y
        draw.line([(x, start_y), (x, start_y + card_h)], fill=C_ACCENT, width=2 * S)
        return y

    def _compute_item_positions(self, draw, items: list, start_y: int) -> list:
        positions: list = []
        heights = [self._measure_item_v2(draw, it) for it in items]
        ROW_GAP = 24 * SCALE
        row_start_y = start_y
        for i, _it in enumerate(items):
            row = i // NUM_COLS
            col = i % NUM_COLS
            if col == 0 and i > 0:
                prev_row_start = (row - 1) * NUM_COLS
                prev_row_end = min(prev_row_start + NUM_COLS, len(items))
                row_max = max(heights[prev_row_start:prev_row_end])
                row_start_y += row_max + ROW_GAP
            x = MARGIN_X + col * (COL_W + COL_GAP)
            positions.append((x, row_start_y))
        return positions

    def _draw_section_items(self, draw, y: int, items: list) -> int:
        if not items:
            return y
        positions = self._compute_item_positions(draw, items, start_y=y)
        heights = [self._measure_item_v2(draw, it) for it in items]
        for (x, iy), item in zip(positions, items):
            self._draw_item_v2(draw, x, iy, item)
        last_row_start_y = positions[-1][1]
        last_row_first = ((len(items) - 1) // NUM_COLS) * NUM_COLS
        last_row_max_h = max(heights[last_row_first:])
        return last_row_start_y + last_row_max_h + 8 * SCALE

    # ── Footer ───────────────────────────────────────
    def _draw_footer_v2(self, draw, y: int) -> int:
        S = SCALE
        x1, x2 = MARGIN_X, PAGE_W - MARGIN_X
        cx = PAGE_W // 2
        y += 22 * S
        y = _double_rule(draw, x1, x2, y)
        y += 14 * S
        role = self.fonts_v2["footer"]
        footer = "Daybreak  ·  AI-Powered Tech Intelligence  ·  github.com/Autumn1337/Daybreak"
        _draw_centered_run(draw, cx, y, footer, role, C_MUTED)
        y += _line_height_role(draw, role) + 4 * S
        return y

    # ── Grouping ─────────────────────────────────────
    @staticmethod
    def _group_by_category(items: list) -> list:
        buckets: dict = {c: [] for c in CATEGORY_ORDER}
        for it in items:
            cat = _normalize_category(it.get("category"))
            buckets[cat].append(it)
        return [(c, buckets[c]) for c in CATEGORY_ORDER if buckets[c]]
