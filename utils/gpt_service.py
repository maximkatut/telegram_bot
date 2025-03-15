import os

import openai
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("OPENAI_TOKEN")
token = 'sk-proj-' + token[:3:-1] if token.startswith('gpt:') else token

openai.api_key = token


class ChatGPTService:
    def __init__(self):
        self.history = []

    def set_system_message(self, content):
        self.history.append({
            'role': "system",
            'content': content
        })

    def add_assistant_message(self, content):
        self.history.append({
            'role': "assistant",
            'content': content
        })

    def add_user_message(self, content):
        self.history.append({
            'role': "user",
            'content': content
        })

    def get_response(self):
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.history,
            max_tokens=1000
        )
        assistant_reply = response.choices[0].message.content
        self.add_assistant_message(assistant_reply)
        return assistant_reply

    @staticmethod
    def get_random_fact_response():
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "Tell me some random fact, it should be one sentence"
                }
            ]
        )
        return completion.choices[0].message.content
