from langchain_groq import ChatGroq

from app.config.logging import logger
from app.config.settings import settings


class LLMService:
    """Service responsible for interacting with the LLM."""

    def __init__(self) -> None:
        self.llm = ChatGroq(
            model=settings.llm_model,
            groq_api_key=settings.groq_api_key,
            temperature=0.2,
        )

    def generate_response(
        self,
        message: str,
    ) -> str:
        """Generate a response from the LLM."""

        logger.info("Sending request to Groq")
        logger.debug("Prompt length: %d characters", len(message))

        response = self.llm.invoke(message)

        logger.info("Received response from Groq")
        logger.debug(
            "Response length: %d characters",
            len(response.content),
        )

        return response.content