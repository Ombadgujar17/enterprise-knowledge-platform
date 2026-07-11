from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import settings


class ChromaStore:
    """Handles persistence of document embeddings in ChromaDB."""

    def __init__(
        self,
        embedding_model: HuggingFaceEmbeddings,
    ) -> None:
        self.vector_store = Chroma(
            collection_name="enterprise_documents",
            embedding_function=embedding_model,
            persist_directory=settings.chroma_db_path,
        )

    def add_documents(self, documents) -> None:
        """Store documents in ChromaDB."""

        self.vector_store.add_documents(documents)