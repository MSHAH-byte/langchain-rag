from sentence_transformers import CrossEncoder


def create_reranker():
    return CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(query, documents, reranker, top_k=5):
    pairs = [
        [query, document.page_content]
        for document in documents
    ]

    scores = reranker.predict(pairs)

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True
    )

    return [document for document, score in ranked_documents[:top_k]]