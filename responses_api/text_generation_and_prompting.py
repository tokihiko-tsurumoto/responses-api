# https://platform.openai.com/docs/guides/text?api-mode=responses

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)

print(response)
