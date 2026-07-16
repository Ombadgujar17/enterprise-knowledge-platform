from app.tools.tool_registry import ToolRegistry


class ToolService:
    """
    Service responsible for tool execution.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def execute(
        self,
        intent: str,
        query: str,
    ) -> str:
        return self.registry.execute(
            intent=intent,
            query=query,
        )