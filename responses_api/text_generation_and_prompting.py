# https://platform.openai.com/docs/guides/text?api-mode=responses

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Talk like a pirate.",  # only applies to the current response generation request
    input="Are semicolons optional in JavaScript?",
)

# developer message enable to persist the same model instructions across the turn
# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=[
#         {"role": "developer", "content": "Talk like a pirate."},
#         {"role": "user", "content": "Are semicolons optional in JavaScript?"},
#     ],
# )

print(response.output_text)
