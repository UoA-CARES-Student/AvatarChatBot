import os
import openai

API_KEY = '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'


def chat(message):
    openai.api_key = API_KEY
    completion = openai.Completion.create(engine="curie", prompt = "what is your favourite animal?",
    temperature=0.4, stop=['\nHuman'], top_p=1, frequency_penalty=0,presence_penalty=0.1,best_of=1)

    response = completion.choices[0].text.strip()
    print(f"response is {response}")

    return response