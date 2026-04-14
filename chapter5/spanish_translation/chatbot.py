from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()
llm = OpenAI()

user_input = input("Enter a phrase and I'll translate it to Spanish!\n")

response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=0,
    input=f"Translate the following to Spanish: {user_input}"
)   

print(response.output_text)