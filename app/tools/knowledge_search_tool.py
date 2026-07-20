from app.tools.base import BaseTool


class KnowledgeSearchTool(BaseTool):
    """
    Enterprise Knowledge Search Tool.

    Later this will call the RAG pipeline.
    """

    def execute(
        self,
        query: str,
    ) -> str:
        return (
            "Knowledge Search Tool\n\n"
            f"Query: {query}\n\n"
            "RAG integration coming next."
        )