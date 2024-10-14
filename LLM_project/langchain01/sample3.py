from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "아이폰 13 출시일을 알려줘"
        },
        
    ]
)

print(json.dumps(chat_completion.choices[0].message.content, indent=2, ensure_ascii=False))