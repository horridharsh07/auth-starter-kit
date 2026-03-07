from fastapi import FastAPI
from app.core.config import settings
from app.api.auth import router as auth_router



app= FastAPI(
    title="Auth-Starter-Kit-API",
    description="A starter kit for building authentication APIs with FastAPI.",
    version="1.0.0",
)
@app.get("/")
def health_check():
    return {"message": "Auth-Starter-Kit-API is running!"}

app.include_router(auth_router)

