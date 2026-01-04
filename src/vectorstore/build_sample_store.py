import pandas as pd
import sys
import os
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma

# Ensure 'src' is in path
root_path = Path(os.getcwd())
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from src.config import (
    PROCESSED_DATA_DIR,
    SAMPLE_VECTOR_STORE
)
from src.embeddings.chunking import get_text_splitter
from src.embeddings.embedder import load_embedding_model
from src.utils.logging import get_logger

logger = get_logger(__name__)

def stratified_sample(df, n_samples=12000):
    """
    Improved stratified sampling with safety checks for small categories.
    """
    n_categories = df["Product"].nunique()
    samples_per_cat = int(n_samples / n_categories)
    
    logger.info(f"Sampling ~{samples_per_cat} records per product category.")
    
    return (
        df.groupby("Product", group_keys=False)
        .apply(lambda x: x.sample(
            n=min(len(x), samples_per_cat),
            random_state=42
        ))
    )

def build_sample_vectorstore():
    try:
        # 1. Load Data
        data_path = PROCESSED_DATA_DIR / "filtered_complaints.csv"
        if not data_path.exists():
            raise FileNotFoundError(f"Missing processed data at {data_path}. Run Task 1 first.")
            
        df = pd.read_csv(data_path)
        logger.info(f"Loaded {len(df)} records from {data_path}")

        # 2. Sample
        df_sample = stratified_sample(df)
        
        # 3. Process Documents
        splitter = get_text_splitter()
        documents = []

        for _, row in df_sample.iterrows():
            # Handle potential empty narratives
            narrative = str(row.get("clean_narrative", ""))
            if not narrative or narrative == "nan":
                continue

            chunks = splitter.split_text(narrative)
            
            for i, chunk in enumerate(chunks):
                documents.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "complaint_id": str(row.get("Complaint ID", "unknown")),
                            "product": row["Product"],
                            "issue": row.get("Issue", "unknown"),
                            "company": row.get("Company", "unknown"),
                            "chunk_index": i
                        }
                    )
                )

        logger.info(f"Generated {len(documents)} vector-ready chunks.")

        # 4. Create Vector Store
        embedding_model = load_embedding_model()
        
        # We use 'from_documents' which handles the batch embedding
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            persist_directory=str(SAMPLE_VECTOR_STORE),
            collection_name="complaints_sample"
        )
        
        # In newer LangChain/Chroma versions, persist() is called automatically, 
        # but explicit call ensures safety on older environments.
        vectorstore.persist()
        logger.info(f"✅ SUCCESS: Vector store created at {SAMPLE_VECTOR_STORE}")

    except Exception as e:
        logger.error(f"❌ FAILED to build vector store: {str(e)}")
        raise

if __name__ == "__main__":
    build_sample_vectorstore()