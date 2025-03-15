from transformers import pipeline
import gradio as gr

# Initialize the text generation pipeline for chatbot
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Define chatbot function
def vanilla_chatbot(message, history):
    response = chatbot(message, max_length=100)
    return response[0]['generated_text']

# Create a Gradio interface
demo_chatbot = gr.Interface(
    fn=vanilla_chatbot,
    inputs="text",
    outputs="text",
    title="Vanilla Chatbot",
    description="Enter text to start chatting."
)

# Launch the chatbot
demo_chatbot.launch()
