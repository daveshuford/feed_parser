'''
Run all to create feed 
'''
from pprint import pprint
import db
from models import dataframe

# Pull new feed
update = dataframe.news_feed


# Run in SQL
db.write2sql(update)
