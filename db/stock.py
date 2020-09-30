#from sqlalchemy import create_engine, Column, String, Integer, Date
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Stock(Base):
    """
    Declarative base class 'Stock' to map 
    to database table 'stocks'
    """
    __tablename__ = 'stocks'

    added = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    date = Column(Date, primary_key=True)
    open = Column(DECIMAL(12, 2))
    close = Column(DECIMAL(12, 2))
    high = Column(DECIMAL(12, 2))
    low = Column(DECIMAL(12, 2))
    volume = Column(Integer)
    change = Column(DECIMAL(5, 2))
    changePercent = Column(DECIMAL(9, 6))
    label = Column(String(length=10))
    changeOverTime = Column(DECIMAL(9,8))

    

 