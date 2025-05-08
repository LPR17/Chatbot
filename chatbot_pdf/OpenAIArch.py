from openai import OpenAI

#Creats instance of OpenAI client to interact w/OpenAI API
client = OpenAI()

#OpenAI API interaction
response = client.chat.completions.create( #Method to retrieve a completion response from the API
    #GPT Model
    model="gpt-4.1",
    #List of dictionaries that represent the convo between user and system
    messages=[
        #Provide the instructions to the AI model to generate the output
        {
            "role":"system",
            "content":"You will be provided with a block of text, and your task is to extract a list of keyword from it"
        },
        #"Input"
        {
            "role":"user",
            "content":
        }
              ],
    #Parameter to control randomness of the generated response (higher temperature == more random and creative output & lower temperature == more focused and deterministic output)
    temperature = 0.5
)


print(response.choices[0].message.content) #message.contet attribute contains the generated response