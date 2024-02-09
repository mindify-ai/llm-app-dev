import gradio as gr
import requests

is_gpt3 = True


def echo_gptchatbot(message, history):
    # Post the message to the server
    response = requests.post(
        "https://markchenx-udemy-genai-app-course.hf.space/api/chat/gpt3", data={"user_request": message}
    )
    # Return the response
    llm_output = response.json()["result"]["content"]

    return llm_output


def echo_llamachatbot(message, history):
    # Post the message to the server
    response = requests.post(
        "https://markchenx-udemy-genai-app-course.hf.space/api/chat/llama", data={"user_request": message}
    )

    # Return the response
    llm_output = response.json()["result"][0]["generated_text"]

    return llm_output


# Create a Gradio interface with the chatbot
if is_gpt3:
    demo = gr.ChatInterface(
        fn=echo_gptchatbot,
        examples=["What is OpenAI?", "What is GPT-3?"],
        title="GPT-3 Chatbot",
    )
else:
    demo = gr.ChatInterface(
        fn=echo_llamachatbot,
        examples=["What is OpenAI?", "What is LLM?"],
        title="LLM Chatbot - Llama 2 7B",
    )

demo.launch()
