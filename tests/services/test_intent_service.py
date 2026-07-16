from app.services.intent_service import IntentService


def test_intent_classifier() -> None:
    service = IntentService()

    assert (
        service.classify("What is the leave policy?")
        == "knowledge_query"
    )

    assert (
        service.classify("Hello!")
        == "general_chat"
    )

    assert (
        service.classify("Create an IT support ticket")
        == "tool_request"
    )