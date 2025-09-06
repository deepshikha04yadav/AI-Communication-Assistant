from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    sender = Column(String)
    subject = Column(String)
    body = Column(Text)
    received_at = Column(DateTime)
    sentiment = Column(String)
    priority = Column(String)
    phone = Column(String, nullable=True)
    alternate_email = Column(String, nullable=True)
    product = Column(String, nullable=True)
    ai_reply = Column(Text, nullable=True)
    resolved = Column(Boolean, default=False)
