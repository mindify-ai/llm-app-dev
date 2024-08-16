import gradio as gr
import requests

is_gpt3 = False


def echo_gptchatbot(message, history):
    # Post the message to the server
    response = requests.post(
        "https://markchenx-udemy-demo-2.hf.space/api/chat/gpt4o/mini", data={"user_request": message}
    )

    return response.json()["result"]


def echo_llamachatbot(message, history):
    # Post the message to the server
    response = requests.post(
        "https://markchenx-udemy-demo-2.hf.space/api/chat/llama", data={"user_request": message}
    )

    return response.json()["result"]


# Create a Gradio interface with the chatbot
if is_gpt3:
    demo = gr.ChatInterface(
        fn=echo_gptchatbot,
        examples=["What is OpenAI?", "What is GPT-3?"],
        title="GPT-4o mini Chatbot",
    )
else:
    demo = gr.ChatInterface(
        fn=echo_llamachatbot,
        examples=["What is OpenAI?", "What is LLM?"],
        title="LLM Chatbot - Llama 2 7B",
    )

demo.launch()
