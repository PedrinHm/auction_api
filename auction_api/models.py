from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    start_bid = Column(Float)
    auction_end = Column(DateTime, default=datetime.utcnow)
    bids = relationship("Bid", back_populates="item")

class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    user = relationship("User", back_populates="bids")
    item = relationship("Item", back_populates="bids")

User.bids = relationship("Bid", order_by=Bid.id, back_populates="user")
