import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # .env 파일 로드
openai_api_key = os.getenv("GROQ_KEY")
llm = ChatGroq(model="llama-3.2-90b-text-preview", api_key=openai_api_key, temperature=0.5)

def getLLM() :
    return llm