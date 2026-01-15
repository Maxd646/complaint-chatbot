import gradio as gr
from src.rag.pipeline import run_rag

def chat(question):
    return run_rag(question)

iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask about customer complaints..."
    ),
    outputs="text",
    title=" CrediTrust Complaint Intelligence Assistant",
    description="Ask questions about customer complaints and receive evidence-based insights."
)

if __name__ == "__main__":
    iface.launch()
