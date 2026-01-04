from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from src.config import VECTOR_STORE_DIR

def load_retriever(k: int = 5):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=VECTOR_STORE_DIR,
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    return retriever
