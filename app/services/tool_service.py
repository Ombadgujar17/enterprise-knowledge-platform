from app.services.llm_service import LLMService
from app.tools.tool_registry import ToolRegistry


class ToolService:
    """
    Service responsible for selecting and executing enterprise tools.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()
        self.llm = LLMService()

    def _select_tool(
        self,
        query: str,
    ) -> str:
        """
        Use the LLM to determine which tool should be executed.
        """

        prompt = f"""
You are an enterprise AI tool router.

Available tools:

- ticket
- leave
- email
- search

Routing Rules:

- IT issue -> ticket
- Password reset -> ticket
- VPN -> ticket
- Laptop -> ticket
- Software issue -> ticket
- Printer -> ticket

- Leave request -> leave
- Vacation -> leave
- Sick leave -> leave

- Send email -> email
- Notify -> email

- HR policy -> search
- Company policy -> search
- Employee handbook -> search
- Technical documentation -> search

Return ONLY the tool name.

Question:
{query}
"""

        from app.config.logging import logger

        tool = self.llm.generate_response(prompt).strip().lower()

        logger.info("Selected tool: %s", tool)

        return tool

    def execute(
        self,
        query: str,
    ) -> str:
        tool_name = self._select_tool(query)

        return self.execute_tool(
            tool_name=tool_name,
            query=query,
        )

    def execute_tool(
        self,
        tool_name: str,
        query: str,
    ) -> str:
        """
        Execute a specific tool directly.
        """

        return self.registry.execute(
            tool_name=tool_name,
            query=query,
        )