from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful eCommerce customer support assistant."
    ),
    (
        "user",
        "{question}"
    )
])

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

chain = prompt | llm

response = chain.invoke({
    "question": "My order has not arrived. What should I do?"
})

print(response.content)