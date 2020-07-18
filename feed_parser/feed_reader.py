'''
Run all to create feed = possible, convert to class? .. but also have the second half.
Take in _tables_ and cascade the update
'''
from pprint import pprint
import db
from models import dataframe

# Pull new feed
update = dataframe.news_feed


# Run in SQL
db.write2sql(update)