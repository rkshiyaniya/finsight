from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String, nullable=True)