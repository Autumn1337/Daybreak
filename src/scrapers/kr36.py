"""36Kr news flash scraper."""

import logging
from datetime import datetime, timezone
from typing import List

import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models import ContentItem, SourceType, Kr36Config

logger = logging.getLogger(__name__)

BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


class Kr36Scraper(BaseScraper):
    """Scraper for 36Kr newsflashes."""

    def __init__(self, config: Kr36Config, http_client: httpx.AsyncClient):
        super().__init__(config.__dict__, http_client)
        self.kr36_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        # Note: 36Kr newsflashes don't expose precise timestamps.
        # published_at is set to now(); since-filtering is not possible.
        # Deduplication relies on URL-based cross-run filtering.
        try:
            resp = await self.client.get(
                "https://36kr.com/newsflashes",
                headers={"User-Agent": BROWSER_UA},
                timeout=10,
            )
            resp.raise_for_status()
        except httpx.HTTPError as e:
            logger.warning("36Kr fetch failed: %s", e)
            return []

        soup = BeautifulSoup(resp.text, "html.parser")
        items = []

        for item in soup.select(".newsflash-item"):
            try:
                title_el = item.select_one(".item-title")
                if not title_el:
                    continue
                title = title_el.get_text(strip=True)
                href = title_el.get("href", "")
                time_el = item.select_one(".time")
                time_str = time_el.get_text(strip=True) if time_el else ""

                url = f"https://36kr.com{href}" if not href.startswith("http") else href

                items.append(ContentItem(
                    id=self._generate_id("kr36", "flash", str(hash(url))),
                    source_type=SourceType.KR36,
                    title=title,
                    url=url,
                    content="",
                    published_at=datetime.now(timezone.utc),
                    metadata={"time_label": time_str, "feed_name": "36Kr"},
                ))
            except (AttributeError, KeyError, TypeError) as e:
                logger.debug("36Kr parse error: %s", e)
                continue

        return items[: self.kr36_config.limit]
