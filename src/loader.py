from langchain_community.document_loaders import PyPDFLoader


def load_documents():
    loader = PyPDFLoader("data/thesis.pdf")
    return loader.load()