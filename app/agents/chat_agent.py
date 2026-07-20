from app.agents.base import BaseAgent
from app.graph.state import AgentState
from app.services.llm_service import LLMService


class ChatAgent(BaseAgent):

    def __init__(self):
        self.llm = LLMService()

    def run(
        self,
        state: AgentState,
    ) -> AgentState:

        state["response"] = self.llm.generate_response(
            state["question"]
        )

        return state