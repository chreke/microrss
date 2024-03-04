import argparse
import datetime
import sys
import time

import feedparser
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader("generate"),
    autoescape=select_autoescape()
)

def to_datetime(time_struct):
    return datetime.datetime.fromtimestamp(time.mktime(time_struct))

def generate_html(feed_urls):
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
    template = env.get_template("index.html")
    return template.render(entries=entries, last_updated=datetime.datetime.now())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('INFILE', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('OUTFILE', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    feed_urls = []
    with args.INFILE as f:
        for line in f:
            feed_urls.append(line.strip())
    html = generate_html(feed_urls)
    with args.OUTFILE as f:
        f.write(html)


if __name__ == "__main__":
    main()
