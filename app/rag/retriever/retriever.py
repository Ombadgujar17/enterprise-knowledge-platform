from langchain_core.documents import Document

from app.rag.vectorstore.chroma_store import ChromaStore
from app.services.embedding_service import EmbeddingService


class Retriever:
    """Retrieves relevant chunks from ChromaDB."""

    def __init__(self) -> None:
        embedding_service = EmbeddingService()

        self.vector_store = ChromaStore(
            embedding_service.get_embeddings()
        )

    def retrieve(
        self,
        query: str,
        k: int = 8,
    ) -> list[Document]:
        """Retrieve relevant chunks."""

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )