from transformers import pipeline

def load_llm():
    llm = pipeline(
        "text-generation",
        model="mistralai/Mistral-7B-Instruct-v0.2",
        max_new_tokens=300,
        temperature=0.2,
        do_sample=True
    )
    return llm


def generate_answer(llm, prompt: str) -> str:
    response = llm(prompt)[0]["generated_text"]
    return response
