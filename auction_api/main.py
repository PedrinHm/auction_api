from fastapi import FastAPI
from auction_api.routers import items, bids, users
from .database import Base, engine
from . import models

app = FastAPI()

app.include_router(items.router)
app.include_router(bids.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to API"}

def create_tables():
    Base.metadata.create_all(bind=engine)

def init_db():
    models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    init_db()
