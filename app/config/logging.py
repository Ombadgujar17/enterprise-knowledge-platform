import logging

from app.config.settings import settings


def setup_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )


logger = logging.getLogger("enterprise_knowledge_platform")