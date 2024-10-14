from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from settings import getLLM

llm = getLLM()

# 프롬프트 템플릿 설정

prompt = PromptTemplate(
    template="{product} 는 어디에서 개발한 제품인가요?",
    input_variables=["product"]
)

message = [
    HumanMessage(content=prompt.format(product="아이폰"))
]

# chain = prompt | llm | StrOutputParser()
chain = llm | StrOutputParser()
# 프롬프트 실행
# response = chain.invoke({"product" : "아이폰"})
response = chain.invoke(message)
print(message)
print(response)  
