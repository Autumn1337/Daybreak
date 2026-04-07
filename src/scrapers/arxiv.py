"""ArXiv AI/ML paper scraper with 3-tier fallback strategy."""

import asyncio
import re
import logging
from datetime import datetime, timezone
from typing import List

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, ArxivConfig

logger = logging.getLogger(__name__)


class ArxivScraper(BaseScraper):
    """Scraper for ArXiv AI/ML papers with weekend fallback."""

    def __init__(self, config: ArxivConfig, http_client: httpx.AsyncClient):
        super().__init__(config.__dict__, http_client)
        self.arxiv_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        limit = self.arxiv_config.limit
        categories = self.arxiv_config.categories

        # 3-tier fallback: narrow → broad → recently updated
        strategies = [
            ("+OR+".join(f"cat:{c}" for c in categories), "submittedDate"),
            ("+OR+".join(f"cat:{c}" for c in categories) + "+OR+cat:cs.CV+OR+cat:cs.MA", "submittedDate"),
            ("+OR+".join(f"cat:{c}" for c in categories), "lastUpdatedDate"),
        ]

        for i, (query, sort_by) in enumerate(strategies):
            items = await self._query_arxiv(query, sort_by, limit, since)
            if items:
                if i > 0:
                    logger.info("ArXiv: got %d papers using fallback strategy #%d", len(items), i + 1)
                return items
            if i < len(strategies) - 1:
                logger.info("ArXiv: strategy #%d returned 0, trying broader query...", i + 1)
                await asyncio.sleep(2)

        logger.warning("ArXiv: all strategies exhausted, no papers found")
        return []

    async def _query_arxiv(
        self, query: str, sort_by: str, limit: int, since: datetime
    ) -> List[ContentItem]:
        url = (
            f"https://export.arxiv.org/api/query?search_query={query}"
            f"&start=0&max_results={limit}&sortBy={sort_by}&sortOrder=descending"
        )

        try:
            resp = await self.client.get(url, timeout=30)
            xml = resp.text
            if len(xml) < 500:
                return []
        except httpx.HTTPError as e:
            logger.warning("ArXiv fetch failed: %s", e)
            return []

        items = []
        entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)

        for entry in entries:
            arxiv_id_match = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', entry)
            title_match = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
            summary_match = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
            published_match = re.search(r'<published>([^<]+)</published>', entry)
            authors = re.findall(r'<name>([^<]+)</name>', entry)
            categories = re.findall(r'<category term="([^"]+)"', entry)

            if not (arxiv_id_match and title_match):
                continue

            title = title_match.group(1).strip().replace('\n', ' ')
            summary = ' '.join((summary_match.group(1) if summary_match else "").split())
            pub_str = published_match.group(1) if published_match else ""

            try:
                published_at = datetime.fromisoformat(pub_str.replace('Z', '+00:00'))
            except (ValueError, TypeError):
                published_at = datetime.now(timezone.utc)

            items.append(ContentItem(
                id=self._generate_id("arxiv", "paper", arxiv_id_match.group(1)),
                source_type=SourceType.ARXIV,
                title=title,
                url=f"https://arxiv.org/abs/{arxiv_id_match.group(1)}",
                content=summary,
                author=", ".join(authors[:3]),
                published_at=published_at,
                metadata={
                    "arxiv_id": arxiv_id_match.group(1),
                    "categories": categories[:5],
                    "pdf_url": f"https://arxiv.org/pdf/{arxiv_id_match.group(1)}.pdf",
                }
            ))

        return items
