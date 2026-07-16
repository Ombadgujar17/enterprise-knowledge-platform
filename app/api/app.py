from fastapi import FastAPI

from app.api.router import api_router
from app.config.settings import settings
from app.config.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(api_router)