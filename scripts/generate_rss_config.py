"""Convert OPML file to Horizon config.json RSS entries."""

import json
import re
import urllib.request


OPML_URL = "https://gist.githubusercontent.com/emschwartz/e6d2bf860ccc367fe37ff953ba6de66b/raw/hn-popular-blogs-2025.opml"


def fetch_opml() -> str:
    with urllib.request.urlopen(OPML_URL, timeout=15) as resp:
        return resp.read().decode("utf-8")


def parse_opml(content: str) -> list:
    entries = []
    for match in re.finditer(r'<outline[^>]+type="rss"[^>]*>', content):
        outline = match.group(0)
        text = re.search(r'text="([^"]+)"', outline)
        xml_url = re.search(r'xmlUrl="([^"]+)"', outline)
        if text and xml_url:
            entries.append({
                "name": text.group(1),
                "url": xml_url.group(1),
                "enabled": True,
                "category": "hn-blog"
            })
    return entries


def main():
    print("Fetching OPML...")
    content = fetch_opml()
    entries = parse_opml(content)
    print(f"Found {len(entries)} RSS feeds")

    out_path = "data/rss_feeds.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
