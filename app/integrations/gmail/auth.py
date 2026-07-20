from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from app.config.settings import settings

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
]


class GmailAuth:
    """
    Handles Gmail OAuth authentication.
    """

    def get_credentials(self) -> Credentials:
        creds = None

        token_path: Path = settings.gmail_token_path
        credentials_path: Path = settings.gmail_credentials_path

        if token_path.exists():
            creds = Credentials.from_authorized_user_file(
                token_path,
                SCOPES,
            )

        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path,
                    SCOPES,
                )

                creds = flow.run_local_server(port=0)

            token_path.write_text(creds.to_json())

        return creds