from app.graph.builder import build_graph


def test_graph_builds():
    graph = build_graph()

    result = graph.invoke(
        {
            "question": "What is Python?",
            "intent": "",
            "documents": [],
            "prompt": "",
            "response": "",
            
        }
    )

    assert result["intent"] == "knowledge_query"