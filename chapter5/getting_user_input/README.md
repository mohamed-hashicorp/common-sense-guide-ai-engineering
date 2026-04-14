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
I'm a helpful chatbot! Ask me anything: 
Who is the first person landed on the moon?
The first person to land on the Moon was Neil Armstrong. He set foot on the lunar surface on July 20, 1969, during the Apollo 11 mission.
```
