from langchain_core.prompts import ChatPromptTemplate


def create_rag_prompt():
    return ChatPromptTemplate.from_template(
        """Answer the question using only the provided context.

If the answer cannot be found in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer:"""
    )