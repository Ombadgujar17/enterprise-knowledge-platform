from app.agents.base import BaseAgent
from app.graph.state import AgentState
from app.services.rag_service import RAGService


class KnowledgeAgent(BaseAgent):

    def __init__(self):
        self.rag = RAGService()

    def run(
        self,
        state: AgentState,
    ) -> AgentState:

        documents = self.rag.retrieve(
            state["question"]
        )

        prompt = self.rag.build_prompt(
            state["question"],
            documents,
        )

        state["response"] = self.rag.generate(
            prompt
        )

        return state