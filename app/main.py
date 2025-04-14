from fastapi import FastAPI
from app.routes import tasks
from app.database import Base, engine

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routes
app.include_router(tasks.router)
