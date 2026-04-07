"""V2EX hot topics scraper via public JSON API."""

import logging
from datetime import datetime, timezone
from typing import List

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, V2EXConfig

logger = logging.getLogger(__name__)

BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


class V2EXScraper(BaseScraper):
    """Scraper for V2EX hot topics."""

    def __init__(self, config: V2EXConfig, http_client: httpx.AsyncClient):
        super().__init__(config.__dict__, http_client)
        self.v2ex_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                "https://www.v2ex.com/api/topics/hot.json",
                headers={"User-Agent": BROWSER_UA},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, ValueError) as e:
            logger.warning("V2EX fetch failed: %s", e)
            return []

        items = []
        for topic in data:
            if not topic.get("url"):
                continue

            replies = topic.get("replies", 0)
            created = topic.get("created", 0)
            try:
                published_at = datetime.fromtimestamp(created, tz=timezone.utc) if created else datetime.now(timezone.utc)
            except (ValueError, OSError):
                published_at = datetime.now(timezone.utc)

            if published_at < since:
                continue

            items.append(ContentItem(
                id=self._generate_id("v2ex", "topic", str(topic.get("id", ""))),
                source_type=SourceType.V2EX,
                title=topic.get("title", ""),
                url=topic["url"],
                content=topic.get("content", ""),
                author=topic.get("member", {}).get("username", ""),
                published_at=published_at,
                metadata={
                    "replies": replies,
                    "node": topic.get("node", {}).get("title", ""),
                    "feed_name": "V2EX",
                },
            ))

        return items[: self.v2ex_config.limit]
