from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from settings import getLLM

llm = getLLM()

# 프롬프트 템플릿 설정
message = [
    # HumanMessage(content="계란찜 만드는 방법을 알려줘"),
    # AIMessage(content="{ChatModel의 계란찜 만드는 법}"),
    # HumanMessage(content="영어로 번역해줘"),
    SystemMessage(content="당신은 친한 친구 입니다. 존댓말을 쓰지말고 솔직하게 답해주세요."),
    HumanMessage(content="안녕?")
]

chain = llm | StrOutputParser()
# 프롬프트 실행
response = chain.invoke(message)

print(response)  
