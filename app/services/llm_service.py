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

        try:
            response = self.llm.invoke(message)
            return response.content
        except Exception as e:
            raise RuntimeError(f"LLM request failed: {e}")