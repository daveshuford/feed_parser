'''
Process and filter RSS Feed
'''
import pandas as pd
from feed import parser
import datetime

source = parser.raw_feed

def create_feed(source):
    source = pd.DataFrame(data=source)  # Import RSS feed to pandas
    keywords = ['covid-19', 'coronavirus', 'Stimulus', 'Texas', 'Tarrant', 'Richland Hills']
    query = '|'.join(keywords)
    feed = source[source['title'].str.contains(query, case=False)]
    feed = feed.reset_index(drop=True)
    feed['posted'] = pd.to_datetime(feed['posted'])
    #feed['published'] = pd.to_datetime(feed['published'])
    # Create excel file to hold data.
    #feed_file = feed.to_excel('main_feed.xlsx')
    #feed_csv = feed.to_csv('feed.csv', sep= '.')
    #return feed
    return feed


news_feed = create_feed(source)

print(news_feed.info())