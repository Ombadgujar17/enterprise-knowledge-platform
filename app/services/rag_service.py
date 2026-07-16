
from app.rag.retriever.retriever import Retriever
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from langchain_core.documents import Document


class RAGService:
    """Coordinates retrieval and generation."""

    def __init__(self) -> None:
        self.retriever = Retriever()
        self.llm = LLMService()

    def retrieve_documents(
        self,
        question: str,
    ) -> list[Document]:
        """
        Retrieve relevant documents for a question.
        """

        return self.retriever.retrieve(question)
    
    def build_prompt(
        self,
        question: str,
        documents: list[Document],
    ) -> str:
        """
        Build the RAG prompt.
        """

        return PromptService.build_rag_prompt(
            question=question,
            documents=documents,
        )

    def generate_response(
        self,
        prompt: str,
    ) -> str:
        """
        Generate the final answer.
        """

        return self.llm.generate_response(prompt)

    def answer(
        self,
        question: str,
    ) -> str:

        documents = self.retrieve_documents(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = PromptService.build_rag_prompt(
            question=question,
            context=context,
        )

        return self.llm.generate_response(prompt)