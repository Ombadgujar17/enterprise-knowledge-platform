from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Healthy!!"}

@app.get("/health")
def health_check():
    return {"status": "healthy","environmrent": "Development"}
