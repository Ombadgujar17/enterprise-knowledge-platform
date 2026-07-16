from typing import Literal,TypedDict
from langchain_core.documents import Document


class GraphState(TypedDict):
    question: str

    intent: Literal[
        "knowledge_query",
        "general_chat",
        "tool_request",
    ]

    documents: list[Document]

    prompt: str

    response: str