"""Feishu (飞书) webhook notification service."""

import logging
from typing import List, Optional

import httpx

from ..models import ContentItem

logger = logging.getLogger(__name__)

ITEMS_PER_PAGE = 10


def _build_page_card(
    items: List[ContentItem],
    date: str,
    page: int,
    total_pages: int,
    total_fetched: int,
    total_selected: int,
) -> dict:
    """Build a single Feishu card for one page of items."""
    lines = []

    if page == 1:
        lines.append(f"共抓取 {total_fetched} 条，筛选出 {total_selected} 条重要内容\n")

    start = (page - 1) * ITEMS_PER_PAGE
    page_items = items[start:start + ITEMS_PER_PAGE]

    for i, item in enumerate(page_items, start + 1):
        score = item.ai_score or 0
        summary = item.ai_summary or item.title
        if len(summary) > 80:
            summary = summary[:77] + "..."
        source = item.source_type.value
        lines.append(f"**{i}. [{item.title}]({item.url})** ⭐{score:.0f}")
        lines.append(f"{summary}")
        lines.append(f"*{source}*\n")

    content = "\n".join(lines)

    if total_pages > 1:
        title = f"📋 Daybreak 每日速递 — {date} ({page}/{total_pages})"
    else:
        title = f"📋 Daybreak 每日速递 — {date}"

    return {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": title},
                "template": "blue",
            },
            "elements": [{"tag": "markdown", "content": content}],
        },
    }


async def send_feishu_summary(
    webhook_url: str,
    items: List[ContentItem],
    date: str,
    total_fetched: int,
    github_pages_url: Optional[str] = None,
) -> bool:
    """Send daily summary to Feishu group via webhook, paginated.

    Args:
        webhook_url: Feishu bot webhook URL
        items: Important items (already filtered and sorted by score)
        date: Date string (YYYY-MM-DD)
        total_fetched: Total items fetched before filtering
        github_pages_url: Optional link to full report

    Returns:
        True if all pages sent successfully
    """
    if not items:
        return True

    total_pages = (len(items) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    all_ok = True

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            for page in range(1, total_pages + 1):
                card = _build_page_card(
                    items, date, page, total_pages,
                    total_fetched, len(items),
                )
                resp = await client.post(webhook_url, json=card)
                resp.raise_for_status()
                result = resp.json()
                ok = result.get("code") == 0 or result.get("StatusCode") == 0
                if not ok:
                    logger.warning("Feishu page %d/%d failed: %s", page, total_pages, result)
                    all_ok = False

            if github_pages_url:
                link_card = {
                    "msg_type": "interactive",
                    "card": {
                        "header": {
                            "title": {"tag": "plain_text", "content": f"📄 完整报告 — {date}"},
                            "template": "green",
                        },
                        "elements": [{
                            "tag": "action",
                            "actions": [{
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "查看完整报告"},
                                "url": github_pages_url,
                                "type": "primary",
                            }],
                        }],
                    },
                }
                await client.post(webhook_url, json=link_card)

    except Exception as e:
        logger.warning("Feishu notification failed: %s", e)
        return False

    if all_ok:
        logger.info("Feishu notification sent: %d pages", total_pages)
    return all_ok
