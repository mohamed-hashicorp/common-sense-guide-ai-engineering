# Chapter 11 — RAG Chatbot with Query Expansion & Classification

An enhanced RAG chatbot for GROSS software customer support. Extends chapter 10 by adding query expansion and product classification before each retrieval step, improving search relevance.

## Prerequisites

- Python 3.10+
- An OpenAI API key
- A Pinecone API key with a pre-populated index named `gross-app` (namespace: `all-gross`, with a `manual` metadata field per chunk)

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

Type your question and press Enter. Type `exit` to quit.


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
| `.env` | API keys (not committed to version control) |
