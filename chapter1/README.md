# Chapter 1: HeLLMo, World!

- Install uv
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Run the following command
```
$ uv init hello_world
```
- Change directory
```
$ cd hello_world
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
uv run chatbot.py
```
- output will be
```
# uv run chatbot.py
The first person to land on the Moon was **Neil Armstrong**. He set foot on the lunar surface on **July 20, 1969**, during the **Apollo 11** mission. As he stepped onto the Moon, he famously said:

> "That's one small step for [a] man, one giant leap for mankind."

Buzz Aldrin followed him shortly after, becoming the second person to walk on the Moon.
```
- update the model in the chatbot.py
```
model="gpt-4.1-mini"
```
- run the chatbot.py again
```
$ uv run chatbot.py
The first person to land on the Moon was Neil Armstrong. He set foot on the lunar surface on July 20, 1969, during NASA's Apollo 11 mission. His famous words upon stepping onto the Moon were, "That's one small step for [a] man, one giant leap for mankind."
```
- update the model in the chatbot.py
```
model="gpt-5-mini"
```
- run the chatbot.py again
```