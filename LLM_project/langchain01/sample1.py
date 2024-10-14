import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_KEY"),
)

chat_completion = client.chat.completions.create(
    # model="llama3-70b-8192",
    model="llama-3.2-90b-text-preview",
    messages=[
        {
            "role": "user",
            "content": "아이폰 13 출시일이 언제야?",
        }
    ],
    max_tokens=100, #생성할 문장의 최대 토큰 수
    temperature=0.5, #생성할 문장의 다양성을 나타내는 매개변수 --> 0~2 ( 높을 수록 다양성 증가 => 가사 / 이야기, 낮을 수록 다양성 감소 => 논리성 중시 )
    n=1,#생성할 문장의 수 
)

print(json.dumps(chat_completion.choices[0].message.content, indent=2, ensure_ascii=False))