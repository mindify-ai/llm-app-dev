import os
from openai import OpenAI

client = OpenAI(
    organization=os.environ["OpenAI_ORG_ID"],
)


def chatbot(user_request:str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_request},
        ],
    )

    return completion.choices[0].message
