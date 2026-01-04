from langchain_community.embeddings import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL_NAME


def load_embedding_model():
    """
    Loads and returns the embedding model
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
