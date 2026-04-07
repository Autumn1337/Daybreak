"""Daily summary generation — pure programmatic rendering."""

import re
from collections import OrderedDict
from typing import List, Dict

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Daybreak Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "header_sub": "From {total} items, {selected} important content pieces were selected",
        "empty_sub": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Daybreak 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "header_sub": "从 {total} 条内容中，筛选出 {selected} 条重要资讯",
        "empty_sub": "分析了 {total} 条内容，暂无达到重要性阈值的内容。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


CATEGORY_ORDER = ["AI/ML", "Security", "Dev Tools", "Systems", "Industry", "Research", "Other"]

CATEGORY_LABELS = {
    "en": {
        "AI/ML": "AI / Machine Learning", "Security": "Security",
        "Dev Tools": "Developer Tools", "Systems": "Systems & Infrastructure",
        "Industry": "Industry News", "Research": "Research", "Other": "Other",
    },
    "zh": {
        "AI/ML": "AI / 机器学习", "Security": "安全",
        "Dev Tools": "开发工具", "Systems": "系统与基础设施",
        "Industry": "行业动态", "Research": "研究", "Other": "其他",
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['header_sub'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        # Group items by category, preserving score order within each group
        grouped: OrderedDict[str, List[ContentItem]] = OrderedDict()
        for item in items:
            cat = item.ai_category or "Other"
            grouped.setdefault(cat, []).append(item)

        cat_labels = CATEGORY_LABELS.get(language, CATEGORY_LABELS["en"])

        # Build TOC and body grouped by category
        toc_lines: List[str] = []
        body_parts: List[str] = []
        idx = 0

        for cat in CATEGORY_ORDER:
            if cat not in grouped:
                continue
            cat_items = grouped[cat]
            cat_display = cat_labels.get(cat, cat)

            toc_lines.append(f"**{cat_display}**")
            for item in cat_items:
                idx += 1
                _t = item.metadata.get(f"title_{language}") or item.title
                t = str(_t).replace("[", "(").replace("]", ")")
                if language == "zh":
                    t = _pangu(t)
                score = item.ai_score or "?"
                toc_lines.append(f"{idx}. [{t}](#item-{idx}) \u2b50\ufe0f {score}/10")
            toc_lines.append("")

        toc = "\n".join(toc_lines) + "---\n\n"

        idx = 0
        for cat in CATEGORY_ORDER:
            if cat not in grouped:
                continue
            cat_display = cat_labels.get(cat, cat)
            body_parts.append(f"## {cat_display}\n\n")
            for item in grouped[cat]:
                idx += 1
                body_parts.append(self._format_item(item, labels, language, idx))

        return header + toc + "".join(body_parts)

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            day = item.published_at.strftime("%d").lstrip("0")
            source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        lines = [
            f'<a id="item-{index}"></a>',
            f"### [{title}]({url}) \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_sub'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
