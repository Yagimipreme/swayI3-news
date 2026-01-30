import feedparser
import os

#MOST BASIC , working most times
#NO FILTERING YET APPLIED

#RSS FEED URL EXMP
FEED_URL = "https://www.tagesschau.de/infoservices/alle-meldungen-100~rss2.xml"

def get_latest_news():
    feed = feedparser.parse(FEED_URL)
    if feed.entries:
        latest = feed.entries[0]
        # Save url for bar-click event
        with open("/tmp/latest_news_url", "w") as f:
            f.write(latest.link)
        print(latest.title[:50] + "...")
        print(f"[DEBUG] : {latest}")
    else:
        print("No News")

if __name__ == "__main__":
    get_latest_news()
