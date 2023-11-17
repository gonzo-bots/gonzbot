from openai import OpenAI


def gpt(prompt, key):
    client = OpenAI(api_key=key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message.content
    return result



