
from dotenv import load_dotenv
import openai
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
print("API KEY cargada:", os.getenv("OPENAI_API_KEY") is not None)

with open("pdf-text.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

hotel_assistant_template = prompt + """
You are the hotel manager of Landon Hotel, named "Mr. Landon". 
Your expertise is exclusively in providing information and advice about anything related to Landon Hotel. 
This includes any general Landon Hotel related queries. 
You do not provide information outside of this scope. 
If a question is not about Landon Hotel, respond with, "I can't assist you with that, sorry!" 
Question: {question} 
Answer: 
"""

hotel_assistant_prompt_template = PromptTemplate(
    input_variables=["question"],
    template=hotel_assistant_template
)

llm = OpenAI(
    model='gpt-3.5-turbo-instruct',
    temperature=0
)

llm_chain = hotel_assistant_prompt_template | llm

def query_llm(question):
    print(f"Mr. Landon: {llm_chain.invoke({'question': question})}")

print("🟢 Landon Hotel Assistant ready. Write your answer:")
while True:
    try:
        user_input = input(">")
        query_llm(user_input)
    except Exception as e:
        print(f"Error: {e}")

