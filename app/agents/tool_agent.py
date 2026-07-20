from app.agents.base import BaseAgent
from app.graph.state import AgentState
from app.services.tool_service import ToolService


class ToolAgent(BaseAgent):

    def __init__(self):
        self.tool_service = ToolService()

    def run(
        self,
        state: AgentState,
    ) -> AgentState:

        state["response"] = self.tool_service.execute(
            state["question"]
        )

        return state