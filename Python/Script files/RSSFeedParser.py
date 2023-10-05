import feedparser

'''Description: This program reads and parses RSS feeds from a URL using the 
feedparser library and displays the latest news headlines.'''

def read_rss_feed(url):
    try:
        feed = feedparser.parse(url)
        if feed.entries:
            print("Latest News Headlines:")
            for entry in feed.entries:
                print(f"- {entry.title}")
        else:
            print("No news found in the feed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
read_rss_feed(rss_url)