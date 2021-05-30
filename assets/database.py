# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import datetime
import pandas as pd

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
engine = create_engine(os.environ.get('DATABASE_URL') or 'sqlite:///' + databese_file, convert_unicode=True , echo=True)
db_session = scoped_session(
                sessionmaker(
                    autocommit = False,
                    autoflush = False,
                    bind = engine
                )
             )
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import assets.models
    Base.metadata.create_all(bind=engine)

def read_data():
    from assets import models

    df = pd.read_csv('assets/data.csv')
    for index, _df in df.iterrows():
        date = datetime.datetime.strptime(_df['date'], '%Y/%m/%d').date()
        row = models.Data(date=date, subscribers=_df['subscribers'], reviews=_df['reviews'])
        db_session.add(row)
    db_session.commit()
