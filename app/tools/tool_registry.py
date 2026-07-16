from app.tools.ticket_tool import TicketTool


class ToolRegistry:
    """
    Registry of enterprise tools.
    """

    def __init__(self) -> None:
        self.ticket_tool = TicketTool()

    def execute(
        self,
        intent: str,
        query: str,
    ) -> str:
        """
        Execute the correct tool.
        """

        if intent == "tool_request":
            return self.ticket_tool.execute(query)

        raise ValueError(f"Unknown tool intent: {intent}")