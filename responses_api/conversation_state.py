# https://platform.openai.com/docs/guides/conversation-state?api-mode=responses

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="ジョークを話してください。",
)
print(response.output_text)

second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "なぜこれが面白いのか説明してください。"}],
)
print(second_response.output_text)

# response.id and second_response.id will be same value.
