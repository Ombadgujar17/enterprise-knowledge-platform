from langchain_groq import ChatGroq


from app.config.settings import settings


class LLMService:
    """Service responsible for interacting with the LLM."""

    def __init__(self) -> None:
        self.llm = ChatGroq(
            model=settings.llm_model,
            groq_api_key=settings.groq_api_key,
            temperature=0.2,
        )

    def generate_response(self, message: str) -> str:
        """Generate a response from the LLM."""
    
        print("\n========== PROMPT SENT TO GROQ ==========\n")
        print(message)

        response = self.llm.invoke(message)

        print("\n========== RESPONSE FROM GROQ ==========\n")
        print(response.content)

        return response.content