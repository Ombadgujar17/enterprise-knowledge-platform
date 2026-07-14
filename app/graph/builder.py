from app.graph.nodes import GraphNodes
from app.graph.workflow import build_workflow
from app.services.rag_service import RAGService


def build_graph():
    """
    Create and compile the LangGraph workflow.
    """

    rag_service = RAGService()

    nodes = GraphNodes(
        rag_service=rag_service,
    )

    workflow = build_workflow(nodes)

    return workflow.compile()