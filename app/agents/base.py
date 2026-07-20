from abc import ABC, abstractmethod

from app.graph.state import AgentState


class BaseAgent(ABC):
    """
    Base class for all agents.
    """

    @abstractmethod
    def run(
        self,
        state: AgentState,
    ) -> AgentState:
        ...