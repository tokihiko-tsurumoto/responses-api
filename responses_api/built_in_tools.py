# https://platform.openai.com/docs/guides/tools?api-mode=responses

from openai import OpenAI

client = OpenAI()

# Tools available in the OpenAI platform are Web search, File search, Computer use, Function calling.
response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="今日の良いニュースは何でしたか？",
)

print(response.output_text)
