#from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Stock(Base):
    """
    Declarative base class 'Stock' to map 
    to database table 'stocks'
    """
    __tablename__ = 'stocks'

    date = Column(Date, primary_key=True)
    open = Column(DECIMAL)
    close = Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    volume = Column(Integer)
    change = Column(DECIMAL)
    changePercent = Column(DECIMAL)
    label = Column(String)
    changeOverTime = Column(DECIMAL)


