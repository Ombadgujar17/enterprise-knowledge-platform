import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from app.integrations.gmail.auth import GmailAuth


class GmailService:
    """
    Service responsible for interacting with the Gmail API.
    """

    def __init__(self):
        credentials = GmailAuth().get_credentials()
        self.service = build(
            "gmail",
            "v1",
            credentials=credentials,
        )

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> str:
        message = MIMEText(body)

        message["to"] = recipient
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        sent_message = (
            self.service.users()
            .messages()
            .send(
                userId="me",
                body={"raw": raw_message},
            )
            .execute()
        )

        return sent_message["id"]