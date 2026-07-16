from app.graph.builder import build_graph


def test_general_chat_path() -> None:
    graph = build_graph()

    result = graph.invoke(
        {
            "question": "Hello!",
            "intent": "",
            "documents": [],
            "prompt": "",
            "response": "",
        }
    )

    assert result["intent"] == "general_chat"
    assert result["response"] != ""