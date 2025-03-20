# https://platform.openai.com/docs/quickstart?api-mode=responses

from openai import OpenAI

client = OpenAI()

# Create a response
create_response = client.responses.create(
    model="gpt-4o-mini",
    input="ユニコーンに関する寝かしつけの物語を3文で話してください。",
)
id = create_response.id
print(create_response)

# List input items
input_items_response = client.responses.input_items.list(id)
print(input_items_response)

# Retrieve a response by id
get_response = client.responses.retrieve(id)
print(get_response)

# Delete a response by id
client.responses.delete(id)
