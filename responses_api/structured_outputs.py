# https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses

import json

from openai import OpenAI

client = OpenAI()

# Structured Outputs is the evolution of JSON mode.
# While both ensure valid JSON is produced, only Structured Outputs ensure schema adherance.
response = client.responses.create(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "イベント情報を抽出します。"},
        {
            "role": "user",
            "content": "アリスとボブは金曜日に科学フェアに行く予定です。",
        },
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "calendar_event",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "date": {"type": "string"},
                    "participants": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["name", "date", "participants"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    },
)

event = json.loads(response.output_text)
