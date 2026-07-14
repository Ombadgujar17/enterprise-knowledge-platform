from app.graph.state import GraphState
from app.services.rag_service import RAGService


class GraphNodes:
    """
    Contains all LangGraph node implementations.

    Each node receives the shared GraphState,
    updates it, and returns it.
    """

    def __init__(
        self,
        rag_service: RAGService,
    ) -> None:
        self.rag_service = rag_service

    def classify_intent(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Phase 11:
        Every request is treated as a knowledge query.
        """

        state["intent"] = "knowledge_query"

        return state
    
    def retrieve_documents(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Retrieve relevant documents from the vector store.
        """

        state["documents"] = self.rag_service.retrieve_documents(
            state["question"]
        )

        return state