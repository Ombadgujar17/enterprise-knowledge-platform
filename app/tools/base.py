from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all enterprise tools.
    """

    @abstractmethod
    def execute(
        self,
        query: str,
    ) -> str:
        ...