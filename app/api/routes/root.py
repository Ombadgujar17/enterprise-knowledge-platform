from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }