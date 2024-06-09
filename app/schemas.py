from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class BidBase(BaseModel):
    value: float

class BidCreate(BidBase):
    user_id: int
    item_id: int

class Bid(BidBase):
    id: int
    user_id: int
    item_id: int
    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    title: str
    description: str
    start_bid: float

class ItemCreate(ItemBase):
    auction_end: datetime

class Item(ItemBase):
    id: int
    bids: List[Bid] = []
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    bids: List[Bid] = []
    class Config:
        from_attributes = True
