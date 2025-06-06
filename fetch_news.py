import json
import os
from datetime import datetime
import feedparser


def fetch_from_feed(url: str, limit: int = 5):
    """Fetch latest items from an RSS/Atom feed."""
    parsed = feedparser.parse(url)
    entries = []
    for item in parsed.entries[:limit]:
        entries.append({
            "source": url,
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "published": item.get("published", "")
        })
    return entries


def append_news(entries, file_path: str = "news.json"):
    """Append news items to a JSON file."""
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.extend(entries)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    sources = [
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "https://news.google.com/rss/search?q=AI&hl=en-US&gl=US&ceid=US:en",
        "http://feeds.bbci.co.uk/news/technology/rss.xml"
    ]
    all_entries = []
    for url in sources:
        all_entries.extend(fetch_from_feed(url, limit=5))
    append_news(all_entries)
    print(f"Fetched and stored {len(all_entries)} items.")
