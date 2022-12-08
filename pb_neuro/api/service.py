import openai
import os

OAI_TOKEN = os.environ.get('OAI_TOKEN', '')


def make_gpt_resp(prompt: str, tokens: int = 200, n: int = 1) -> str:
    openai.api_key = OAI_TOKEN
    response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=400,
            n=n
        )
    return '\n\n'.join([choice.text.strip() for choice in response.choices])
