from app.services.rag_service import RAGService


class ChatService:
    """Service responsible for chat."""

    def __init__(self) -> None:
        self.rag_service = RAGService()

    def chat(
        self,
        message: str,
    ) -> str:

        return self.rag_service.answer(message)