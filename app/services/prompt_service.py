from langchain_core.documents import Document


class PromptService:
    """Builds prompts for the LLM."""

    @staticmethod
    def build_rag_prompt(
        question: str,
        documents: list[Document],
    ) -> str:
        """
        Build a Retrieval-Augmented Generation prompt.
        """

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        return f"""
You are an AI Knowledge Assistant for an enterprise.

Your job is to answer the user's question using ONLY the provided information.

Guidelines:

1. Write your answer naturally, as if you are talking to a colleague.
2. Do NOT mention "context", "documents", or "retrieved information".
3. Do NOT copy large sections verbatim.
4. Summarize and explain in your own words.
5. If the answer is not contained in the provided information, clearly state that you could not find the answer in the available information.
6. Never make up facts that are not supported by the provided information.

Information:
{context}

Question:
{question}

Answer:
"""