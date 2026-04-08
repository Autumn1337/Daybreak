from datetime import datetime, timezone

from src.ai.newspaper import NewspaperRenderer
from src.models import ContentItem, SourceType


def test_newspaper_renderer_falls_back_when_truetype_is_unavailable(monkeypatch) -> None:
    monkeypatch.setattr("src.ai.newspaper._font_path_candidates", lambda *names: [])

    item = ContentItem(
        id="rss:test:1",
        source_type=SourceType.RSS,
        title="Fallback font smoke test",
        url="https://example.com/item-1",
        content="content",
        author="tester",
        published_at=datetime.now(timezone.utc),
    )
    item.ai_score = 8.5
    item.ai_summary = "Renderer should still produce a PNG when custom fonts are missing."
    item.ai_category = "AI/ML"

    renderer = NewspaperRenderer()
    image = renderer.render([item], "2026-04-08", total_fetched=1, language="en")

    assert image.startswith(b"\x89PNG\r\n\x1a\n")
