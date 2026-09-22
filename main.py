from src.loader import load_documents
from src.chunker import split_documents
from src.embeddings import create_embeddings
from src.vectorstore import create_vectorstore
from src.reranker import create_reranker, rerank_documents
from src.prompt import create_rag_prompt
from src.generator import create_llm
from src.chain import create_rag_chain


documents = load_documents()
chunks = split_documents(documents)

embeddings = create_embeddings()
vectorstore = create_vectorstore(chunks, embeddings)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 10}
)

reranker = create_reranker()
llm = create_llm()
prompt = create_rag_prompt()

rag_chain = create_rag_chain(prompt, llm)


print("\nEduAI RAG Assistant")
print("Ask questions about the thesis.")
print("Type 'exit' or 'quit' to quit.\n")


while True:
    question = input("Ask a question: ").strip()

    if question.lower() in {"exit", "quit"}:
        print("\nGoodbye!")
        break

    if not question:
        continue

    retrieved_documents = retriever.invoke(question)

    reranked_documents = rerank_documents(
        question,
        retrieved_documents,
        reranker,
        top_k=5
    )

    context = "\n\n".join(
        document.page_content
        for document in reranked_documents
    )

    response = rag_chain.invoke({
        "context": context,
        "question": question
    })

    print("\nAnswer:")
    print(response.content)

    print(
        f"\nRetrieved candidates: {len(retrieved_documents)}"
        f" | After reranking: {len(reranked_documents)}\n"
    )