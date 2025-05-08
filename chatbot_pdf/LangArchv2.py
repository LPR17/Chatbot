from flask import Flask, render_template, request, jsonify
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
    response = llm_chain.invoke({'question': question})
    return response

app = Flask(__name__)#Creates new flask appliaction instance

#Define root dor the root URL
@app.route("/")
def index():
    return render_template('index.html') #Renders the html template

#Define route for the chatbot endpoint, it will accept the post request
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json() #When a POST request is sent to this endpoint the json data is retrieved using this command
    question = data["question"] #Question value fromt the JSON data is extracted and stored in this variable
    response = query_llm(question) #Call to the query_llm function , it helps generating the response from the LLM
    return jsonify({"response": response}) #The response is returned as a JSON object

#Debug code
if __name__ == "__main__":
    app.run(debug=True)