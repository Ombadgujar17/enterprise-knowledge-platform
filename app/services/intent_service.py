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
          You are an enterprise intent classifier.

          Your job is to classify the user's request into EXACTLY ONE of these intents.

          Allowed intents:

          - knowledge_query
          - general_chat
          - tool_request

          Definitions:

          knowledge_query
          - The user is asking for information that should be retrieved from company documents.
          - Examples:
              - What is the leave policy?
              - Explain the onboarding process.
              - What is the reimbursement policy?
              - Show the HR manual.
              - What does the employee handbook say?

          general_chat
          - Greetings.
          - Casual conversation.
          - General AI questions.
          - Questions that do not require company knowledge or performing actions.
          - Examples:
              - Hello
              - Good morning
              - How are you?
              - Tell me a joke.
              - Explain Python.

          tool_request
          - The user wants the system to DO something.
          - Examples:
              - Create a ticket.
              - Reset my password.
              - My laptop is broken.
              - VPN is not working.
              - Printer issue.
              - Send an email.
              - Notify HR.
              - Apply for leave.
              - Schedule a meeting.
              - Raise an incident.

          Return ONLY ONE of:

          knowledge_query
          general_chat
          tool_request

          User:

          {question}
        """

        intent = self.llm.generate_response(prompt).strip()

        logger.info(
            "Intent classified as: %s",
            intent,
        )

        return intent