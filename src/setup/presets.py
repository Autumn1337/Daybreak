"""Preset source library loader and keyword matching."""

import json
from pathlib import Path
from typing import List, Dict, Tuple


def load_presets(presets_path: str = "data/presets.json") -> Dict:
    """Load the presets.json file.

    Args:
        presets_path: Path to the presets JSON file.

    Returns:
        Parsed presets dictionary.

    Raises:
        FileNotFoundError: If the presets file does not exist.
    """
    path = Path(presets_path)
    if not path.exists():
        raise FileNotFoundError(f"Presets file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def match_domains(
    user_input: str,
    presets: Dict,
    threshold: float = 0.1,
) -> List[Tuple[Dict, float]]:
    """Match user interest description against preset domains.

    Performs case-insensitive keyword matching against domain keywords and
    source tags. Returns matched domains sorted by relevance score.

    Args:
        user_input: Free-form user interest description (supports mixed languages).
        presets: Loaded presets dictionary.
        threshold: Minimum score (0–1) to include a domain.

    Returns:
        List of (domain_dict, score) tuples sorted by descending score.
    """
    tokens = set(user_input.lower().split())
    # Also match against the raw input (for multi-word keywords like "deep learning")
    input_lower = user_input.lower()

    results = []
    for domain in presets.get("domains", []):
        score = 0.0
        domain_keywords = [k.lower() for k in domain.get("keywords", [])]
        total_keywords = len(domain_keywords) or 1

        for kw in domain_keywords:
            # Exact token match or substring match
            if kw in tokens or kw in input_lower:
                score += 1.0

        # Also check source-level tags
        for source in domain.get("sources", []):
            for tag in source.get("tags", []):
                if tag.lower() in tokens or tag.lower() in input_lower:
                    score += 0.3

        normalized = min(score / total_keywords, 1.0)
        if normalized >= threshold:
            results.append((domain, normalized))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def collect_sources_from_domains(
    matched_domains: List[Tuple[Dict, float]],
) -> List[Dict]:
    """Flatten matched domains into a deduplicated list of source configs.

    Args:
        matched_domains: Output from match_domains().

    Returns:
        List of source dicts (each with type, description, config, origin="preset").
    """
    seen = set()
    sources = []

    for domain, _score in matched_domains:
        for src in domain.get("sources", []):
            key = _source_unique_key(src)
            if key not in seen:
                seen.add(key)
                sources.append({**src, "origin": "preset"})

    return sources


def _source_unique_key(source: Dict) -> str:
    """Generate a unique key for a source to enable deduplication."""
    src_type = source.get("type", "")
    cfg = source.get("config", {})

    if src_type == "rss":
        return f"rss:{cfg.get('url', '')}"
    elif src_type == "reddit_subreddit":
        return f"reddit:{cfg.get('subreddit', '')}"
    elif src_type == "reddit_user":
        return f"reddit_user:{cfg.get('username', '')}"
    elif src_type == "github_user":
        return f"github_user:{cfg.get('username', '')}"
    elif src_type == "github_repo":
        return f"github_repo:{cfg.get('owner', '')}/{cfg.get('repo', '')}"
    elif src_type == "telegram":
        return f"telegram:{cfg.get('channel', '')}"
    else:
        return f"{src_type}:{json.dumps(cfg, sort_keys=True)}"
