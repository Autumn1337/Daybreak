"""Test that ContentAnalyzer.analyze_batch runs AI calls concurrently."""

import asyncio
import pytest
from unittest.mock import AsyncMock
from datetime import datetime, timezone

from src.ai.analyzer import ContentAnalyzer
from src.models import ContentItem, SourceType


def _make_item(i: int) -> ContentItem:
    return ContentItem(
        id=f"test:item:{i}",
        source_type=SourceType.RSS,
        title=f"Test Item {i}",
        url=f"https://example.com/{i}",
        published_at=datetime.now(timezone.utc),
    )


@pytest.mark.asyncio
async def test_analyze_batch_runs_concurrently():
    """Verify that analyze_batch uses concurrency, not serial execution."""
    call_count = 0
    max_concurrent = 0
    current_concurrent = 0

    async def mock_complete(system, user, temperature=0.3, max_tokens=4096):
        nonlocal call_count, max_concurrent, current_concurrent
        call_count += 1
        current_concurrent += 1
        if current_concurrent > max_concurrent:
            max_concurrent = current_concurrent
        await asyncio.sleep(0.05)  # simulate latency
        current_concurrent -= 1
        return '{"score": 7, "reason": "test", "summary": "test summary", "tags": ["test"]}'

    mock_client = AsyncMock()
    mock_client.complete = mock_complete

    analyzer = ContentAnalyzer(mock_client)
    items = [_make_item(i) for i in range(10)]

    result = await analyzer.analyze_batch(items, concurrency=5)

    assert len(result) == 10
    assert call_count == 10
    # With concurrency=5 and 10 items, max_concurrent should be > 1
    assert max_concurrent > 1, f"Expected concurrent execution, but max_concurrent was {max_concurrent}"
    # All items should have scores
    assert all(item.ai_score == 7.0 for item in result)


@pytest.mark.asyncio
async def test_analyze_batch_handles_failures_gracefully():
    """One item failure should not block others."""
    # Track which item URLs have been seen to make item 2 always fail,
    # regardless of retries (so it exhausts all retry attempts).
    always_fail_url = "https://example.com/2"

    async def mock_complete(system, user, temperature=0.3, max_tokens=4096):
        if always_fail_url in user:
            raise RuntimeError("Simulated API failure")
        return '{"score": 5, "reason": "ok", "summary": "ok", "tags": []}'

    mock_client = AsyncMock()
    mock_client.complete = mock_complete

    analyzer = ContentAnalyzer(mock_client)
    items = [_make_item(i) for i in range(5)]

    result = await analyzer.analyze_batch(items, concurrency=5)

    assert len(result) == 5
    # The failed item should have score 0 (fallback)
    scores = [item.ai_score for item in result]
    assert 0.0 in scores
    # Others should have score 5
    assert scores.count(5.0) >= 3
