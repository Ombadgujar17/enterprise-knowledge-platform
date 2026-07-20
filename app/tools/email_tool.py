from app.config.logging import logger
from app.integrations.gmail.gmail_service import GmailService
from app.models.email import EmailRequest
from app.services.llm_service import LLMService


class EmailTool:
    """Tool responsible for sending emails using Gmail."""

    def __init__(self) -> None:
        self.gmail_service = GmailService()
        self.llm_service = LLMService()

    def _extract_email(
        self,
        query: str,
    ) -> EmailRequest:
        """
        Extract email details from a natural language request.
        """

        logger.info("Extracting email details from user request.")

        prompt = f"""
You are an email extraction assistant.

Extract the following information from the user's request:

- recipient
- subject
- body

Return the information using the provided schema.

User request:

{query}
"""

        email = self.llm_service.structured_output(
            prompt=prompt,
            schema=EmailRequest,
        )

        logger.info("Email details extracted successfully.")

        return email

    def execute(
        self,
        query: str,
    ) -> str:
        """
        Send an email based on a natural language request.
        """

        email = self._extract_email(query)

        logger.info(
            "Sending email to %s",
            email.recipient,
        )

        message_id = self.gmail_service.send_email(
            recipient=email.recipient,
            subject=email.subject,
            body=email.body,
        )

        logger.info(
            "Email sent successfully. Message ID: %s",
            message_id,
        )

        return (
            f"Email sent successfully.\n"
            f"Recipient: {email.recipient}\n"
            f"Subject: {email.subject}\n"
            f"Message ID: {message_id}"
        )