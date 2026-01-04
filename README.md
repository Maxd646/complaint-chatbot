#  Intelligent Complaint Analysis for Financial Services (CrediTrust)

### Transforming Raw Customer Feedback into Strategic Insights

CrediTrust Financial is a mobile-first digital finance company serving over 500,000 users.
This project delivers a Retrieval-Augmented Generation (RAG)–powered chatbot that enables
internal teams to extract insights from large-scale customer complaints in minutes.

---

##  Business Context & KPIs

**Problem:** Manual complaint analysis across Credit Cards, Personal Loans, Savings Accounts,
and Money Transfers is slow and error-prone.

**KPIs**

- Reduce trend identification time from days to minutes
- Enable non-technical users to query 464K+ complaints
- Proactively detect compliance and product risks

---

##  RAG System Architecture

1. Data Ingestion & Cleaning (Task 1)
2. Vector Indexing with Embeddings (Task 2)
3. Semantic Retrieval (Task 3)
4. Grounded Answer Generation with LLMs (Task 4)

---

##  Full Project Folder Structure

##  Full Project Folder Structure

````text
rag-complaint-chatbot/
│
├── .vscode/
│   └── settings.json                 # Editor configuration
│
├── .github/
│   └── workflows/
│       └── unittests.yml             # CI pipeline for automated tests
│
├── data/
│   ├── raw/                          # Original CFPB complaint dataset (not tracked)
│   └── processed/                   # Cleaned & filtered complaint data (Task 1)
│       └── filtered_complaints.csv
│
├── vector_store/                     # Persisted ChromaDB / FAISS indices (Task 2 & 3)
│
├── notebooks/
│   ├── __init__.py
│   ├── eda.ipynb                     # Exploratory Data Analysis (Task 1)
│   └── README.md                     # Notebook documentation
│
├── src/
│   ├── __init__.py
│   │
│   ├── config.py                     # Central configuration (paths, models)
│   │
│   ├── preprocess/
│   │   ├── __init__.py
│   │   └── preprocess.py             # Data cleaning & filtering logic (Task 1)
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedder.py               # Embedding model loader
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   └── build_sample_store.py     # Chunking & indexing pipeline (Task 2)
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── retriever.py              # Semantic retrieval logic (Task 3)
│   │   ├── prompt.py                 # Prompt templates
│   │   ├── generator.py              # LLM interface
│   │   └── pipeline.py               # End-to-end RAG pipeline (Task 3)
│   │
│   └── utils/
│       ├── __init__.py
│       └── logging.py                # Centralized logging utilities
│
├── tests/
│   ├── __init__.py
│   └── test_retriever.py             # Unit tests
│
├── app.py                            # Gradio interactive UI (Task 4)
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Ignored files & directories
└── README.md                         # Project documentation

##  Installation & Setup

```bash
git clone https://github.com/your-username/rag-complaint-chatbot.git
cd rag-complaint-chatbot
pip install -r requirements.txt
````

### Run Tasks 1 & 2

```powershell
$env:PYTHONPATH="."
python src/preprocess/preprocess.py
python -m src.vectorstore.build_sample_store
```

### Launch Chatbot (Task 4)

```bash
python app.py
```

---

##  Key Technical Choices

| Component  | Choice           | Reason                 |
| ---------- | ---------------- | ---------------------- |
| Embeddings | all-MiniLM-L6-v2 | Fast & accurate        |
| Vector DB  | ChromaDB         | Metadata persistence   |
| Chunking   | 500 / 50 overlap | Context balance        |
| Prompting  | Analyst-grade    | Prevent hallucinations |

---

##  License

Educational and internal-use only.
