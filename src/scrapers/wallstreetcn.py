"""WallStreetCN (华尔街见闻) news scraper via JSON API."""

import logging
from datetime import datetime, timezone
from typing import List

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, WallStreetCNConfig

logger = logging.getLogger(__name__)

API_URL = "https://api-one.wallstcn.com/apiv1/content/information-flow?channel=global-channel&accept=article&limit=30"


class WallStreetCNScraper(BaseScraper):
    """Scraper for WallStreetCN news."""

    def __init__(self, config: WallStreetCNConfig, http_client: httpx.AsyncClient):
        super().__init__(config.__dict__, http_client)
        self.wscn_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        try:
            resp = await self.client.get(API_URL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, ValueError) as e:
            logger.warning("WallStreetCN fetch failed: %s", e)
            return []

        items = []
        for entry in data.get("data", {}).get("items", []):
            res = entry.get("resource")
            if not res:
                continue
            title = res.get("title") or res.get("content_short")
            if not title:
                continue

            uri = res.get("uri", "")
            ts = res.get("display_time", 0)
            try:
                published_at = datetime.fromtimestamp(ts, tz=timezone.utc) if ts else datetime.now(timezone.utc)
            except (ValueError, OSError):
                published_at = datetime.now(timezone.utc)

            if published_at < since:
                continue

            items.append(ContentItem(
                id=self._generate_id("wallstreetcn", "article", str(hash(uri))),
                source_type=SourceType.WALLSTREETCN,
                title=title,
                url=uri if uri.startswith("http") else f"https://wallstreetcn.com/articles/{uri}",
                content=res.get("content_short", ""),
                published_at=published_at,
                metadata={"feed_name": "华尔街见闻"},
            ))

        return items[: self.wscn_config.limit]
