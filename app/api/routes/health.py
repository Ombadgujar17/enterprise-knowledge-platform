from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.app_env,
    }