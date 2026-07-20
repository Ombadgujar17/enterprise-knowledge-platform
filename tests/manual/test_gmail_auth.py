from app.integrations.gmail.auth import GmailAuth

auth = GmailAuth()

credentials = auth.get_credentials()

print("Authenticated!")
print(credentials.valid)