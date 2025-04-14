# app/main.py
from fastapi import FastAPI
from app.routes import tasks  # Import the auth routes

app = FastAPI()

# Include the routes
app.include_router(tasks.router)
