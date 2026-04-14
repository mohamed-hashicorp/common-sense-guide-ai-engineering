# Chapter 5: Build a chat bot

- Install uv
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```
- run the commands
```
$ uv add python-dotenv
$ uv add openai
```
- create a `.env` file and set the following
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```
- run the code
```
uv run --with openai --with python-dotenv chatbot.py 
```
- output will be
```
Assistant: How can I help you today?

User: Who was the first person to land on the Moon?
Assistant: The first person to land on the Moon was Neil Armstrong. He set foot on the lunar surface on July 20, 1969, during the Apollo 11 mission.

User: Who was the second?
Assistant: The second person to land on the Moon was Buzz Aldrin. He followed Neil Armstrong and stepped onto the lunar surface shortly after Armstrong on July 20, 1969, during the Apollo 11 mission.

User: exit
```
