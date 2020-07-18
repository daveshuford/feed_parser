'''
CONNECT TO SQL_DB AND WRITE TO TABLE
'''
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Shuford@00536898@localhost/rss_feed')

def write2sql(df):
    df.to_sql('article_feed', con = engine, if_exists = 'append', chunksize = 1000, index=False)