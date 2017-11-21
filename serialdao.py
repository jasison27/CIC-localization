from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float

Base = declarative_base()

class SerialData(Base):
    __tablename__ = 'serial'
    id = Column(Integer,primary_key= True)
    tagID = Column(Integer,index=True)
    sequence = Column(Integer)
    distance = Column(String)
    velocity = Column(String)
    voltage =Column(Float)
    temperature = Column(Integer)
    angle = Column(Float)
    create_time = Column(DateTime)

