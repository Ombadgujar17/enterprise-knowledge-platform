import logging

from app.config.settings import settings


def setup_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )


logger = logging.getLogger("enterprise_knowledge_platform")