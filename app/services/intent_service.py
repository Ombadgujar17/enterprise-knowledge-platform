from app.config.logging import logger
from app.services.llm_service import LLMService


class IntentService:
    """
    Classifies the user's intent.
    """

    def __init__(self) -> None:
        self.llm = LLMService()

    def classify(
        self,
        question: str,
    ) -> str:
        """
        Classify the user's intent.
        """

        logger.info("Starting intent classification")

        prompt = f"""
You are an intent classifier.

Classify the user's request into EXACTLY ONE category.

Categories:

knowledge_query
general_chat
tool_request

Rules:

- knowledge_query:
  Questions that require information from enterprise documents.

- general_chat:
  Greetings, casual conversation, or questions that do not require document retrieval.

- tool_request:
  Requests to perform an action, such as creating tickets, sending notifications,
  scheduling meetings, or executing a task.

Return ONLY the category.

User:

{question}
"""

        intent = self.llm.generate_response(prompt).strip()

        logger.info(
            "Intent classified as: %s",
            intent,
        )

        return intent