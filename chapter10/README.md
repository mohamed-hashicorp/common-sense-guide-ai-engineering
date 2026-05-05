# Chapter 10 — RAG Chatbot

A terminal-based AI customer support chatbot for fictional GROSS software products. It uses OpenAI `gpt-4.1-mini` for responses and Pinecone for retrieval-augmented generation (RAG).

## Prerequisites

- Python 3.10+
- An OpenAI API key
- A Pinecone API key with a pre-populated index named `gross-app` (namespace: `all-gross`)

## Setup

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install openai pinecone python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in this directory:

```
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

## Running the chatbot

Make sure the virtual environment is activated, then run:

```bash
python chatbot.py
```

The chatbot will greet you and wait for your input. Type your question and press Enter. Type `exit` to quit.

## How it works

1. **RAG lookup** — for each user message, the chatbot queries Pinecone to retrieve the top 3 relevant documentation chunks from the `all-gross` namespace.
2. **System prompt injection** — the retrieved chunks are injected into the system prompt so the model only uses documented information to answer.
3. **Citation enforcement** — the model is instructed to prefix every factual point with a `[[chunk-id]]` citation. These tags are stripped before printing to the user.
4. **Multi-turn memory** — the full conversation history is maintained in memory and sent with every request.

## Supported GROSS products

- **Flamehamster** — web browser
- **Rumblechirp** — email client
- **GuineaPigment** — SVG drawing tool
- **EMRgency** — electronic medical record system
- **Verbiage++** — content management system

## Files

| File | Description |
|------|-------------|
| `chatbot.py` | Main chatbot script |
| `traces.csv` | Sample conversation traces used for evaluation |
| `.env` | API keys (not committed to version control) |
