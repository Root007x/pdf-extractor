import os
import json
from langchain_groq import ChatGroq

# load JSON data
def load_json():
    with open("output.json", "r") as file:
        data = json.load(file)
    return data

# save the summary text to summary.txt
def save_summary(response):
    with open("summary.txt", "w") as file:
        file.write(response)
        

# Load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

# Load the Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the ChatGroq language model
llm = ChatGroq(
    api_key=groq_api_key,
    model = "llama-3.3-70b-versatile"
)

# prompt for the language model, including the loaded JSON data
prompts = f"""You are an AI assistant that summarizes corporate audit filings into plain English.
Generate a 3-5 line summary from the following JSON data for a non-technical user.

json data : {load_json()}
"""


if __name__ == "__main__":
    response = llm.invoke(prompts) # Invoke the model
    save_summary(response.content) # save response




