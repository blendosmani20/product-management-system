
from fastapi import FastAPI

app = FastAPI(
    title="Product Management System",
    description="API for managing products",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Product Management System API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
