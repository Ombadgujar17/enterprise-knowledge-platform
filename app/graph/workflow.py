from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState
from app.graph.nodes import GraphNodes


def build_workflow(
    nodes: GraphNodes,
):
    """
    Build the LangGraph workflow.
    """

    workflow = StateGraph(GraphState)

    # Register nodes
    workflow.add_node(
        "classify_intent",
        nodes.classify_intent,
    )

    workflow.add_node(
        "retrieve_documents",
        nodes.retrieve_documents,
    )

    # Define graph flow
    workflow.add_edge(
        START,
        "classify_intent",
    )

    workflow.add_edge(
        "classify_intent",
        "retrieve_documents",
    )

    workflow.add_edge(
        "retrieve_documents",
        END,
    )

    return workflow