# https://platform.openai.com/docs/guides/text?api-mode=responses

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="海賊のように話しなさい。",  # only applies to the current response generation request
    input="JavaScript ではセミコロンはオプションですか？",
)

# developer message enable to persist the same model instructions across the turn
# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=[
#         {"role": "developer", "content": "海賊のように話しなさい。"},
#         {"role": "user", "content": "JavaScript ではセミコロンはオプションですか？"},
#     ],
# )

print(response.output_text)
