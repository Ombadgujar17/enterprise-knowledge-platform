from app.graph.nodes import GraphNodes
from app.graph.workflow import build_workflow
from app.services.rag_service import RAGService
from app.services.intent_service import IntentService
from app.services.tool_service import ToolService


def build_graph():
    """
    Create and compile the LangGraph workflow.
    """

    rag_service = RAGService()
    intent_service = IntentService()
    tool_service = ToolService()

    nodes = GraphNodes(
        rag_service=rag_service,
        intent_service=intent_service,
        tool_service=tool_service,
    )

    workflow = build_workflow(nodes)

    return workflow.compile()