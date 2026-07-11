from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import settings


class ChromaStore:
    """Handles persistence and retrieval of document embeddings."""

    def __init__(
        self,
        embedding_model: HuggingFaceEmbeddings,
    ) -> None:
        self.vector_store = Chroma(
            collection_name=settings.chroma_collection_name,
            embedding_function=embedding_model,
            persist_directory=settings.chroma_db_path,
        )

    def add_documents(
        self,
        documents: list[Document],
    ) -> None:
        """Store documents in ChromaDB."""

        self.vector_store.add_documents(documents)

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ) -> list[Document]:
        """Retrieve the most similar chunks."""

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )