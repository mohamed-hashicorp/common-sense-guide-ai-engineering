import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

model = os.getenv("MODEL", "gpt-4.1")

response = llm.responses.create(
    model=model,
    temperature=0,
    input="Who was the first person to land on the moon",
)

print(response.output_text)