# main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Register the routes
app.include_router(router)
