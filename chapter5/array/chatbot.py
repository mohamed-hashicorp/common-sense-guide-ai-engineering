from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()
llm = OpenAI()

assistant_message = "Assistant: Arrgh, How can I help you, matey?\n\nUser: "
print(f"Assistant: {assistant_message}\n")

user_input = input("User: ")

history =[
    {"role": "developer",
     "content": "You are an AI assistant that responds like a pirate."},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.responses.create(
        model="gpt-4.1-mini",
        temperature=0,
        input=history
    )

    print(f"\n Assistant: {response.output_text}\n")

    user_input = input("User: ")


    history+=[ {"role": "assistant", "content": response.output_text},
                   {"role": "user", "content": user_input} ]
   