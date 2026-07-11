from fastapi import APIRouter

from app.models.retrieval import (
    RetrievalRequest,
    RetrievalResponse,
)
from app.rag.retriever.retriever import Retriever

router = APIRouter(
    prefix="/retrieve",
    tags=["Retrieval"],
)


@router.post(
    "/",
    response_model=RetrievalResponse,
)
def retrieve(
    request: RetrievalRequest,
) -> RetrievalResponse:
    """Retrieve relevant chunks."""

    retriever = Retriever()

    documents = retriever.retrieve(
        request.query,
    )

    return RetrievalResponse(
        chunks=[
            doc.page_content
            for doc in documents
        ]
    )