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
Assistant: Arrgh, How can I help you, matey?

User: Who was the first person to land on the Moon?
Assistant: Arrgh, that be Neil Armstrong, matey! He was the first person to set foot on the Moon on July 20, 1969, durin' the Apollo 11 mission. "That's one small step for man, one giant leap for mankind," he said. What other space adventures can I help ye with?

User: exit
```
