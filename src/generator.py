from langchain_ollama import ChatOllama


def create_llm():
    return ChatOllama(
        model="eduai-finetuned:latest",
        temperature=0
    )