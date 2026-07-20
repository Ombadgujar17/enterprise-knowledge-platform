from typing import Type

from langchain_groq import ChatGroq
from pydantic import BaseModel

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
        """
        Generate a natural language response from the LLM.
        """

        logger.info("Sending request to Groq")
        logger.debug("Prompt length: %d characters", len(message))

        response = self.llm.invoke(message)

        logger.info("Received response from Groq")
        logger.debug(
            "Response length: %d characters",
            len(response.content),
        )

        return response.content

    def structured_output(
        self,
        prompt: str,
        schema: Type[BaseModel],
    ) -> BaseModel:
        """
        Generate structured output validated against a Pydantic model.
        """

        logger.info(
            "Generating structured output using schema: %s",
            schema.__name__,
        )
        logger.debug(
            "Prompt length: %d characters",
            len(prompt),
        )

        structured_llm = self.llm.with_structured_output(schema)

        response = structured_llm.invoke(prompt)

        logger.info(
            "Structured output generated successfully."
        )

        return response