from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

openai_api_key = os.getenv("GROQ_KEY")
llm = ChatGroq(model="llama-3.2-90b-text-preview", api_key=openai_api_key)

# 프롬프트 템플릿 설정
# prompt = PromptTemplate(template="What is the capital of {country}?", input_variables=["country"])
message = [
    HumanMessage(content="안녕?"),
]


# StrOutputParser를 사용하여 출력을 문자열로 파싱
output_parser = StrOutputParser()

# LLM 체인 생성
# chain = LLMChain(llm=llm, prompt=prompt, output_parser=output_parser)
# chain = prompt | llm | output_parser
# chain = message | llm | output_parser
chain = llm | output_parser

# 프롬프트 실행
# response = chain.invoke({"country": "South Korea"})
response = chain.invoke(message)

print(response)  # "Seoul" 과 같은 결과 출력
