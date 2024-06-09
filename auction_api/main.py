from fastapi import FastAPI
from auction_api.routers import items, bids, users
from .database import Base, engine
from . import models
import logging

app = FastAPI()

app.include_router(items.router)
app.include_router(bids.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to API"}

logging.basicConfig(level=logging.INFO)

def create_tables():
    logging.info("Creating tables...")
    Base.metadata.create_all(bind=engine)
    logging.info("Tables created successfully.")

def init_db():
    logging.info("Initializing database...")
    models.Base.metadata.create_all(bind=engine)
    logging.info("Database initialized successfully.")

if __name__ == "__main__":
    create_tables()
    init_db()
