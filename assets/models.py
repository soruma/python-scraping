# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from assets.database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):
    #TableNameの設定
    __tablename__ = "data"
    #Column情報を設定する
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False)
    subscribers = Column(Integer, unique=False)
    reviews = Column(Integer, unique=False)
    timestamp = Column(DateTime, default=dt.now())

    def __init__(self, date=None, subscribers=None, reviews=None, timestamp=None):
        self.date = date
        self.subscribers = subscribers
        self.reviews = reviews
        self.timestamp = timestamp
