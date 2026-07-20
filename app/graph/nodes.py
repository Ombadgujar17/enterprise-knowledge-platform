from app.config.logging import logger

from app.graph.state import GraphState
from app.services.rag_service import RAGService
from app.services.intent_service import IntentService
from app.services.tool_service import ToolService


class GraphNodes:
    """
    Contains all LangGraph node implementations.

    Each node receives the shared GraphState,
    updates it, and returns it.
    """

    def __init__(
        self,
        rag_service: RAGService,
        intent_service: IntentService,
        tool_service: ToolService,
    ) -> None:
        self.rag_service = rag_service
        self.intent_service = intent_service
        self.tool_service = tool_service

    def classify_intent(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Phase 11:
        Every request is treated as a knowledge query.
        """
        logger.info(
            "Executing node: classify_intent"
            )

        state["intent"] = self.intent_service.classify(
            state["question"]
            )
        
        logger.info(
            "Detected intent: %s",
            state["intent"],
            )

        return state
    
    def retrieve_documents(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Retrieve relevant documents from the vector store.
        """

        logger.info(
            "Executing node: retrieve_documents"
            )

        state["documents"] = self.rag_service.retrieve_documents(
            state["question"]
        )

        logger.info(
            "Retrieved %d documents",
            len(state["documents"]),
            )

        return state
    
    def build_prompt(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Build the LLM prompt.
        """
        logger.info(
            "Executing node: build_prompt"
            )

        state["prompt"] = self.rag_service.build_prompt(
            question=state["question"],
            documents=state["documents"],
        )

        logger.info(
            "Prompt created successfully"
            )

        return state
    
    def generate_response(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Generate the final answer.
        """

        logger.info(
            "Executing node: generate_response"
            )

        state["response"] = self.rag_service.generate_response(
            state["prompt"]
        )

        logger.info(
            "Response generated successfully"
            )
        
        return state
    
    def general_chat(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Handle general conversation without document retrieval.
        """

        logger.info(
            "Executing node: general_chat"
            )

        prompt = f"""
        You are a friendly Enterprise AI Assistant.

        Respond naturally and professionally.

        User:

        {state["question"]}
        """



        state["response"] = self.rag_service.generate_response(
            prompt
        )

        logger.info(
            "General chat response generated successfully"
            )

        return state
    
    def execute_tool(
        self,
        state: GraphState,
    ) -> GraphState:
        """
        Execute enterprise tools.
        """

        logger.info(
            "Executing tool for intent: %s",
            state["intent"],
        )

        state["response"] = self.tool_service.execute(
            query=state["question"],
)       

        logger.info(
            "Tool execution completed"
        )

        return state