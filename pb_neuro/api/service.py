import openai
import os
from pb_neuro import schemas

OAI_TOKEN = os.environ.get('OAI_TOKEN', '')


def make_gpt_resp(params: schemas.TextGPT) -> str:
    openai.api_key = OAI_TOKEN
    response = openai.Completion.create(
            model='text-davinci-003',
            prompt=params.prompt,
            temperature=0.9,
            max_tokens=params.tokens,
            n=params.quantity
        )
    return '\n\n'.join([choice.text.strip() for choice in response.choices])
