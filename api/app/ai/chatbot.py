import os
from openai import OpenAI
import requests

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

client = OpenAI(
    organization=os.getenv("OPENAI_ORG_ID"), api_key=os.getenv("OPENAI_API_KEY")
)


def gpt_chatbot(user_request: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_request},
        ],
    )

    return completion.choices[0].message.content    


def llama_chatbot(user_request: str):
    response = requests.post(API_URL, headers=headers, json={"inputs": user_request})

    return response.json()[0]["generated_text"]
