import os
import openai
import datetime
import math
import base64

apiKey = base64.b64decode('c2stNWlveXNISWdST0lqenJpd0xMZFpUM0JsYmtGSnQ2aHVzV3NPN1JkdXVCSVpBM09x')
openai.api_key = apiKey

class gptAdventure:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "you are the writer of a text based adventure game"}
        ]

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"]
