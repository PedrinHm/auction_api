from fastapi import FastAPI
from auction_api.routers import items, bids, users
from .database import Base, engine
from . import models

app = FastAPI()

app.include_router(items.router)
app.include_router(bids.router)
app.include_router(users.router)

if __name__ == "__main__":
    create_tables()
    import uvicorn
    uvicorn.run("auction_api.main:app", host="0.0.0.0", port=8000)  
    
def init_db():
    models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

def create_tables():
    Base.metadata.create_all(bind=engine)