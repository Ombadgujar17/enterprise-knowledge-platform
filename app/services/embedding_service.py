from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import settings


class EmbeddingService:
    """Creates embedding models."""

    def __init__(self) -> None:
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=settings.embedding_model,
        )

    def get_embeddings(self) -> HuggingFaceEmbeddings:
        """Return the configured embedding model."""

        return self.embedding_model