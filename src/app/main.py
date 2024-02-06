import gradio as gr
import requests

def echo(message, history):
    # Post the message to the server
    response = requests.post("http://127.0.0.1:8000/api/chat/gpt3", data={"user_request": message})
    # Return the response
    llm_output = response.json()["result"]['content']
    
    return llm_output
    
demo = gr.ChatInterface(fn=echo, examples=["What is OpenAI?", "What is LLM?"], title="LLM Chatbot")

demo.launch()