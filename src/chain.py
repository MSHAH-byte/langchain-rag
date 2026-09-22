from langchain_core.runnables import Runnable


def create_rag_chain(prompt, llm) -> Runnable:
    return prompt | llm