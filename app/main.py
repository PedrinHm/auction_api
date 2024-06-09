from fastapi import FastAPI
from app.routers import items, bids, users
from .database import Base, engine
from . import models
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"]   # Permite todos os cabeçalhos
)

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
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

