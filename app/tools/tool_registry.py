from app.tools.base import BaseTool
from app.tools.ticket_tool import TicketTool
from app.tools.leave_tool import LeaveTool
from app.tools.email_tool import EmailTool
from app.tools.knowledge_search_tool import KnowledgeSearchTool


class ToolRegistry:
    """
    Registry for all enterprise tools.
    """

    def __init__(self) -> None:
        self.tools: dict[str, BaseTool] = {
            "ticket": TicketTool(),
            "leave": LeaveTool(),
            "email": EmailTool(),
            "search": KnowledgeSearchTool(),
        }

    def execute(
        self,
        tool_name: str,
        query: str,
    ) -> str:
        """
        Execute the requested tool.
        """

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(f"Unknown tool: {tool_name}")

        return tool.execute(query)