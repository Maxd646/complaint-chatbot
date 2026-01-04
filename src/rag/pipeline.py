from src.rag.retriever import load_retriever
from src.rag.prompt import RAG_PROMPT
from src.rag.generator import load_llm, generate_answer

def run_rag(question: str):
    retriever = load_retriever(k=5)
    llm = load_llm()

    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join(
        [f"- {doc.page_content}" for doc in docs]
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = generate_answer(llm, prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": docs
    }
