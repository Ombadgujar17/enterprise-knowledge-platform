from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState
from app.graph.nodes import GraphNodes

def route_intent(state: GraphState) -> str:
    """
    Route execution based on the detected intent.
    """

    return state["intent"]

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

    workflow.add_node(
        "build_prompt",
        nodes.build_prompt,
    )

    workflow.add_node(
        "generate_response",
        nodes.generate_response,
    )

    workflow.add_node(
        "general_chat",
        nodes.general_chat,
    )

    workflow.add_node(
        "execute_tool",
        nodes.execute_tool,
    )

    # Define graph flow
    workflow.add_edge(
        START,
        "classify_intent",
    )

    workflow.add_conditional_edges(
        "classify_intent",
        route_intent,
        {
            "knowledge_query": "retrieve_documents",
            "general_chat": "general_chat",
            "tool_request": "execute_tool",
        },
    )

    workflow.add_edge(
        "retrieve_documents",
        "build_prompt",
    )

    workflow.add_edge(
        "build_prompt",
        "generate_response",
    )

    workflow.add_edge(
         "general_chat",
         END,
    )

    workflow.add_edge(
        "execute_tool",
        END,
    )

    workflow.add_edge(
        "generate_response",
        END,
    )

    return workflow