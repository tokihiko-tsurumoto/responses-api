# https://platform.openai.com/docs/guides/tools?api-mode=responses

import json

import requests
from openai import OpenAI


# tool function
def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    # if name == "send_email":
    #     return send_email(**args)


client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"},
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

input_messages = [{"role": "user", "content": "今日のパリと東京の天気はどうですか？"}]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools,
)

# Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several.
for tool_call in response.output:
    if tool_call.type != "function_call":
        continue

    input_messages.append(tool_call)  # append model's function call message
    name = tool_call.name
    args = json.loads(tool_call.arguments)

    result = call_function(name, args)
    input_messages.append(
        {
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": str(result),
        }
    )


response_2 = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
)
print(response_2.output_text)
