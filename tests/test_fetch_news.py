import os
import json
import tempfile
import unittest

from fetch_news import fetch_from_feed, append_news

class FetchNewsTestCase(unittest.TestCase):
    def test_fetch_from_feed(self):
        url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
        items = fetch_from_feed(url, limit=1)
        self.assertTrue(len(items) > 0)
        self.assertIn("title", items[0])
        self.assertIn("link", items[0])

    def test_append_news(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "news.json")
            entries = [
                {
                    "source": "test",
                    "title": "t",
                    "link": "l",
                    "published": "p"
                }
            ]
            append_news(entries, file_path=path)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "t")

if __name__ == "__main__":
    unittest.main()
