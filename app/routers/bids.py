from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime 
from .. import models, schemas, database

router = APIRouter(
    prefix="/bids",
    tags=["bids"]
)

@router.post("/", response_model=schemas.Bid)
def create_bid(bid: schemas.BidCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == bid.item_id).first()
    
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    if db_item.auction_end < datetime.utcnow():
        raise HTTPException(status_code=400, detail="O leilão deste item já acabou")
    
    last_bid = db.query(models.Bid).filter(models.Bid.item_id == bid.item_id).order_by(models.Bid.value.desc()).first()
    
    if last_bid and bid.value <= last_bid.value:
        raise HTTPException(status_code=400, detail="O valor do lance deve ser maior que o último lance")
    
    db_bid = models.Bid(**bid.dict())
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid

