
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드
parser = StrOutputParser()

openai_api_key = os.getenv("GROQ_KEY")

model = ChatGroq(model="llama-3.2-90b-text-preview", api_key=openai_api_key)

messages = [
    # SystemMessage(content="Translate the following from English into Korean"),
    HumanMessage(content="안녕?"),
]

result = model.invoke(messages)
print(result)