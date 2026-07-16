from app.tools.base import BaseTool


class TicketTool(BaseTool):
    """
    Mock IT ticket tool.
    """

    def execute(
        self,
        query: str,
    ) -> str:
        return (
            "✅ IT Support Ticket Created\n\n"
            f"Request: {query}\n\n"
            "Ticket ID: INC-1001"
        )