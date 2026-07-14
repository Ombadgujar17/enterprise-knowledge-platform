from typing import TypedDict
from langchain_core.documents import Document


class GraphState(TypedDict):
    question: str

    intent: str

    documents: list[Document]

    prompt: str

    response: str