import datetime
import time

import feedparser
from jinja2 import Environment, PackageLoader, select_autoescape

FEED_FILE = "feeds.txt"

env = Environment(
    loader=PackageLoader("generate"),
    autoescape=select_autoescape()
)

def to_datetime(time_struct):
    return datetime.datetime.fromtimestamp(time.mktime(time_struct))

def generate_html(entries):
    template = env.get_template("index.html")
    with open("index.html", "w") as f:
        f.write(template.render(entries=entries))

def main():
    feed_urls = []
    with open(FEED_FILE) as f:
        for line in f:
            feed_urls.append(line.strip())
    entries = []
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            entries.append({
                "feed_title": feed.feed.title,
                "feed_link": feed.feed.link,
                "title": entry.title,
                "link": entry.link,
                "published": to_datetime(entry.published_parsed),
                "source": feed_url
            })
    entries.sort(key=lambda x: x["published"], reverse=True)
    generate_html(entries)


if __name__ == "__main__":
    main()
