import chromadb
from src.config import VECTOR_STORE_DIR

# 1. Connect to the persistent database you just built
client = chromadb.PersistentClient(path=str(VECTOR_STORE_DIR / "sample_chroma"))

# 2. Get the collection (ensure the name matches your build script)
collection = client.get_collection(name="complaints_sample")

# 3. Print the results
print(f"✅ Success! Vector store found at: {VECTOR_STORE_DIR / 'sample_chroma'}")
print(f"📊 Total document chunks indexed: {collection.count()}")

# 4. Peek at the first entry to see metadata
sample = collection.peek(limit=1)
print(f"🏷️ Metadata Sample: {sample['metadatas'][0]}")