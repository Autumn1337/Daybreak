"""Product Hunt scraper via GraphQL API with hydration fallback."""

import json
import logging
import os
import re
from datetime import datetime, timezone
from typing import List

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, ProductHuntConfig

logger = logging.getLogger(__name__)

BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


class ProductHuntScraper(BaseScraper):
    """Scraper for Product Hunt trending products."""

    def __init__(self, config: ProductHuntConfig, http_client: httpx.AsyncClient):
        super().__init__(config.__dict__, http_client)
        self.ph_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        limit = self.ph_config.limit
        token = os.getenv(self.ph_config.api_token_env)

        if token:
            try:
                return await self._fetch_via_api(token, limit)
            except Exception as e:
                logger.warning("PH API failed: %s, falling back to hydration", e)

        return await self._fetch_via_hydration(limit)

    async def _fetch_via_api(self, token: str, limit: int) -> List[ContentItem]:
        query = """
        query { posts(first: %d, order: VOTES) { edges { node {
            name tagline url votesCount website slug
            topics { edges { node { name } } }
            user { name }
        } } } }
        """ % limit

        resp = await self.client.post(
            "https://api.producthunt.com/v2/api/graphql",
            json={"query": query},
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()

        items = []
        for edge in data.get("data", {}).get("posts", {}).get("edges", []):
            node = edge["node"]
            slug = node.get("slug", "")
            topics = [t["node"]["name"] for t in node.get("topics", {}).get("edges", [])]
            user = node.get("user") or {}

            items.append(ContentItem(
                id=self._generate_id("producthunt", "product", slug),
                source_type=SourceType.PRODUCTHUNT,
                title=node["name"],
                url=f"https://www.producthunt.com/posts/{slug}" if slug else node["url"],
                content=node.get("tagline", ""),
                author=user.get("name", "Unknown"),
                published_at=datetime.now(timezone.utc),
                metadata={
                    "votes": node.get("votesCount", 0),
                    "website": node.get("website"),
                    "topics": topics[:3],
                    "tagline": node.get("tagline", ""),
                }
            ))
        return items

    async def _fetch_via_hydration(self, limit: int) -> List[ContentItem]:
        try:
            resp = await self.client.get(
                "https://www.producthunt.com/",
                headers={"User-Agent": BROWSER_UA},
                timeout=15,
                follow_redirects=True,
            )
            html = resp.text

            match = re.search(
                r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html
            )
            if not match:
                logger.warning("PH: __NEXT_DATA__ not found")
                return []

            data = json.loads(match.group(1))
            apollo = data.get("props", {}).get("pageProps", {}).get("apolloState", {})

            posts = [
                v for k, v in apollo.items()
                if k.startswith("Post:") and isinstance(v, dict) and "votesCount" in v
            ]
            posts.sort(key=lambda x: x.get("votesCount", 0), reverse=True)

            items = []
            for post in posts[:limit]:
                slug = post.get("slug", "")
                items.append(ContentItem(
                    id=self._generate_id("producthunt", "product", slug or post.get("name", "")),
                    source_type=SourceType.PRODUCTHUNT,
                    title=post.get("name", "Unknown"),
                    url=f"https://www.producthunt.com/posts/{slug}" if slug else "https://www.producthunt.com/",
                    content=post.get("tagline", ""),
                    author="Unknown",
                    published_at=datetime.now(timezone.utc),
                    metadata={
                        "votes": post.get("votesCount", 0),
                        "tagline": post.get("tagline", ""),
                    }
                ))
            return items
        except Exception as e:
            logger.warning("PH hydration failed: %s", e)
            return []
