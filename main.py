from app.config.logging import logger, setup_logging

setup_logging()

logger.info("Application started successfully.")
logger.warning("This is a warning.")
logger.error("This is an error.")