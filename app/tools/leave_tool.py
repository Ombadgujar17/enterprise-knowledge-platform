from app.tools.base import BaseTool


class LeaveTool(BaseTool):
    """
    Mock HR Leave Request Tool.
    """

    def execute(
        self,
        query: str,
    ) -> str:
        return (
            "🏖️ Leave Request Submitted\n\n"
            f"Reason: {query}\n\n"
            "Status: Pending Manager Approval"
        )