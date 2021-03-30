from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint
import sqlalchemy
from datetime import datetime
import datetime


def add_comparison(today, first, second, winner):
    DATABASE_LOCATION = "sqlite:///sentiment_analysis.sqlite"
    engine = sqlalchemy.create_engine(DATABASE_LOCATION, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class Sentiment(Base):
        __tablename__ = 'tb_sentiment'

        id = Column(Integer, primary_key=True)
        date = Column(String(14))
        first = Column(String(50))
        second = Column(String(50))
        winner = Column(String(50))

    Base.metadata.create_all(engine)

    comparison = Sentiment(date=today, first=first, second=second, winner=winner)
    session.add(comparison)
    session.commit()

    





    







