from app.integrations.gmail.gmail_service import GmailService

gmail = GmailService()

message_id = gmail.send_email(
    recipient="ombadgujar004@gmail.com",
    subject="Enterprise Knowledge Platform Test",
    body="Hello! This email was sent from my Enterprise Knowledge Platform using the Gmail API.",
)

print("Email sent successfully!")
print(f"Message ID: {message_id}")