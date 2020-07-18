'''
Main Schema
    Creates the primary table
    Primary keys are by unique link - this will be used for a foriegn key when the articles are imported.
'''

from sqlalchemy import Column, Text, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table
from db import engine

Base = declarative_base()

class ArticleFeed(Base):
    __table__ = Table('article_feed', Base.metadata,
                    Column('link', VARCHAR(200), primary_key=True),
                    Column('published',DateTime, nullable=True),
                    #Column('posted', DateTime, nullable=True),
                    Column('summary', Text, nullable=False),
                    Column('title', Text, nullable=False),

                    )
    Base.metadata.create_all(engine)
