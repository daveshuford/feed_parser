# RSS MULTI-FEED PARSER
import feedparser
from feed import urls

url = urls.url

def master_parse(url):
    #  Parse raw feeds from urls
    articles = []
    for site, urls in enumerate(url):
        parsed = feedparser.parse(urls)
        entries = parsed['entries']
        feed = parsed['feed']
        for entry in entries:
            articles.append({
                'link': entry.link,
                'title': entry.title,
                'summary': entry.summary.split('<')[0],  # had to spit the text from the whole link summary
                'published': entry.get('published', ""),
                'posted': feed.get('published', "")
            })
    return articles


raw_feed = master_parse(url)