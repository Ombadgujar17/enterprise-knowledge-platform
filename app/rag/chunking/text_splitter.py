from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.settings import settings

class TextSplitter:
    """Splits LangChain documents into smaller chunks."""

    def __init__(self,) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """Split documents into chunks."""

        return self.text_splitter.split_documents(documents)