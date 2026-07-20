from app.models.email import EmailRequest
from app.services.llm_service import LLMService


def main() -> None:
    llm = LLMService()

    prompt = """
You are an email extraction assistant.

Extract the following information and return it using the provided schema.

User request:

Send an email to ombadgujar004plus@gmail.com

Subject: Deployment Complete

Body:
The deployment finished successfully.
"""

    email = llm.structured_output(
        prompt=prompt,
        schema=EmailRequest,
    )

    print("\nExtracted Email")
    print("----------------------------")
    print(email)
    print("----------------------------")
    print(email.recipient)
    print(email.subject)
    print(email.body)


if __name__ == "__main__":
    main()