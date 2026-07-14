from langchain_core.documents import Document

from app.rag.chunking.text_splitter import TextSplitter
from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.vectorstore.chroma_store import ChromaStore
from app.services.embedding_service import EmbeddingService


class DocumentIndexer:
    """Handles indexing documents into the vector database."""

    def __init__(self) -> None:
        embedding_service = EmbeddingService()

        self.loader = PDFLoader()
        self.splitter = TextSplitter()
        self.vector_store = ChromaStore(
            embedding_service.get_embeddings()
        )

    def index(
        self,
        file_path: str,
    ) -> list[Document]:
        """
        Load, split and index a document.
        """

        documents = self.loader.load(file_path)

        chunks = self.splitter.split_documents(documents)

        self.vector_store.add_documents(chunks)

        return chunks,documents