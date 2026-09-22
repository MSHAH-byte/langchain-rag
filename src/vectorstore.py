from langchain_chroma import Chroma


def create_vectorstore(chunks, embeddings):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="eduai_rag"
    )