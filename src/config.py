from pathlib import Path

# ========================
# Base Paths
# ========================
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

VECTOR_STORE_DIR = BASE_DIR / "vector_store"
SAMPLE_VECTOR_STORE = VECTOR_STORE_DIR / "sample_chroma"
FULL_VECTOR_STORE = VECTOR_STORE_DIR / "full_chroma"

# ========================
# Embeddings & RAG Config
# ========================
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5
