from fastapi import FastAPI
from app.core.config import settings



app= FastAPI(
    title="Auth-Starter-Kit-API",
    description="A starter kit for building authentication APIs with FastAPI.",
    version="1.0.0",
)
@app.get("/")
def health_check():
    return {"message": "Auth-Starter-Kit-API is running!"}

