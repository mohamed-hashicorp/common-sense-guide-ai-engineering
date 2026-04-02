# Chapter 1: HeLLMo, World!

## Signing Up for an LLM-as-a-Service

You'll need an [OpenAI API key](https://platform.openai.com/api-keys) to follow along.

## Creating Our First App

- Install uv
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Initialize the project
```
$ uv init hello_world
```
- Change directory
```
$ cd hello_world
```
- Add dependencies
```
$ uv add python-dotenv
$ uv add openai
```
- Create a `.env` file and set the following
```
OPENAI_API_KEY=your_api_key_goes_here
```
- Run the code
```
$ uv run chatbot.py
```
- Output will be something like
```
The first person to land on the Moon was **Neil Armstrong**. He set foot on the lunar surface on **July 20, 1969**, during the **Apollo 11** mission. As he stepped onto the Moon, he famously said:

> "That's one small step for [a] man, one giant leap for mankind."

Buzz Aldrin followed him shortly after, becoming the second person to walk on the Moon.
```

## Tweaking the Model and Temperature

The model is configurable via the `MODEL` environment variable. Try different models to see how their outputs differ:

- Run with `gpt-4.1` (default)
```
$ uv run chatbot.py
```
- Run with `gpt-4.1-mini`
```
$ MODEL=gpt-4.1-mini uv run chatbot.py
```
- Run with `gpt-5-mini` (a reasoning model — notice it may take longer)
```
$ MODEL=gpt-5-mini uv run chatbot.py
```

Notice how different models produce different responses for the same prompt — varying in length, formatting, and level of detail. Even with `temperature=0`, LLMs don't produce perfectly predictable outputs. You can send the same request repeatedly and potentially get a different result each time.

Try dropping the `temperature` parameter entirely and running the same prompt a few times. You'll likely see more variation in the responses.

## Model Snapshots

Model providers can update an LLM at any time. To avoid unexpected changes, providers offer "snapshots" — specific versions that are guaranteed not to change. For example, you can pin to a snapshot like `gpt-4o-2024-11-20` instead of the generic `gpt-4o`.

## Checking API Usage

Each API call costs money. Check your usage at [platform.openai.com/usage](https://platform.openai.com/usage) to see how many tokens you've consumed and what it cost.
