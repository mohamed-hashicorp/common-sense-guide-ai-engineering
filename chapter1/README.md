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
- Run the commands
```
$ uv add python-dotenv
$ uv add openai
```
- Create a `.env` file and set the following
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```
- Run the code
```
$ uv run chatbot.py
```
- Output will be
```
The first person to land on the Moon was **Neil Armstrong**. He set foot on the lunar surface on **July 20, 1969**, during the **Apollo 11** mission. As he stepped onto the Moon, he famously said:

> "That's one small step for [a] man, one giant leap for mankind."

Buzz Aldrin followed him shortly after, becoming the second person to walk on the Moon.
```

## Comparing models

The model is configurable via the `MODEL` environment variable. Try different models to see how their outputs differ:

- Run with `gpt-4.1-mini` (default)
```
$ uv run chatbot.py
The first person to land on the Moon was Neil Armstrong. He set foot on the lunar surface on July 20, 1969, during NASA's Apollo 11 mission. His famous words upon stepping onto the Moon were, "That's one small step for [a] man, one giant leap for mankind."
```
- Run with `gpt-5-mini`
```
$ MODEL=gpt-5-mini uv run chatbot.py
```

Notice how different models produce different responses for the same prompt — varying in length, formatting, and level of detail. Model selection is one of the first practical decisions you'll make as an AI engineer.
