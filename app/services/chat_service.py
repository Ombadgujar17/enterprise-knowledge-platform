from app.graph.builder import build_graph


class ChatService:
    """Service responsible for chat."""

    def __init__(self) -> None:
        self.graph = build_graph()

    def chat(
        self,
        message: str,
    ) -> str:
        result = self.graph.invoke(
            {
                "question": message,
                "intent": "",
                "documents": [],
                "prompt": "",
                "response": "",
            }
        )

        return result["response"]