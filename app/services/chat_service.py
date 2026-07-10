from app.services.llm_service import LLMService


class ChatService:
    """Service responsible for handling chat requests."""

    def __init__(self) -> None:
        self.llm_service = LLMService()

    def chat(self, message: str) -> str:
        return self.llm_service.generate_response(message)