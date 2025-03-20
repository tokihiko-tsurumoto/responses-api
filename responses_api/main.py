# https://platform.openai.com/docs/api-reference/responses

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="ユニコーンに関する寝かしつけの物語を3文で話してください。",
)

print(response)
