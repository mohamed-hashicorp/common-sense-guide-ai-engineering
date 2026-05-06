# Common Sense Guide to AI Engineering

A practical, chapter-by-chapter guide to AI engineering using modern Python tooling.
Each chapter is a self-contained project you can run independently.

## Chapters

| # | Title | Topics |
|---|-------|--------|
| 1 | [HeLLMo, World!](chapter1/) | First LLM API call, uv, OpenAI Responses API, model comparison, snapshots, API usage |
| 5 | [Build a Chatbot](chapter5/) | System prompts, multi-turn dialogue, conversation history, memory, prompt augmentation |
| 6 | [Context Windows](chapter6/) | Full-document prompting, token counting, markdown generation from PDFs |
| 7 | [Vector Search](chapter7/) | Pinecone index creation, dense embeddings with `llama-text-embed-v2` |
| 8 | [Measuring Quality with Evals](chapter8/) | RAG pipeline, qualitative evaluation, open coding, axial coding, trace generation |
| 10 | [RAG Chatbot](chapter10/) | Retrieval-augmented generation, Pinecone search, citation enforcement, multi-turn RAG |
| 11 | [RAG Chatbot with Query Expansion](chapter11/) | Query expansion, product classification, metadata filtering, improved retrieval |

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager, used in chapters 1 and 5)
- Python 3.10+ (used in chapters 6–10)
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Pinecone API key](https://www.pinecone.io/) (used in chapters 7, 8, 10, and 11)

## Chapter Summaries

### Chapter 1 — HeLLMo, World!
[`chapter1/`](chapter1/)

Your first LLM API call using the OpenAI Responses API. Covers installing `uv`, initializing a project, configuring API keys, and experimenting with different models (`gpt-4.1`, `gpt-4.1-mini`, `gpt-5-mini`) and temperature settings. Also introduces model snapshots and API usage monitoring.

### Chapter 5 — Build a Chatbot
[`chapter5/`](chapter5/)

Six incremental sub-projects that build up a working chatbot from scratch:

| Sub-project | What it adds |
|-------------|-------------|
| `prompt/` | Basic system prompt (pirate persona) |
| `getting_user_input/` | Interactive user input loop |
| `multi_turn_dialogue/` | Conversation history sent with each request |
| `memory/` | Persistent memory across turns |
| `augmenting_prompt/` | Dynamic prompt augmentation |
| `array/` | Conversation history stored as an array |

### Chapter 6 — Context Windows
[`chapter6/`](chapter6/)

Explores how to fit large documents into an LLM's context window. Includes a chatbot that loads a full product manual (`flamehamster.md`) as context, a token counter using `tiktoken`, and a markdown generator that converts PDFs to markdown using `docling`.

### Chapter 7 — Vector Search
[`chapter7/`](chapter7/)

Sets up a Pinecone vector index (`gross-app`) for semantic search using the `llama-text-embed-v2` embedding model. Foundation for the RAG pipelines used in chapters 8 and 10.

### Chapter 8 — Measuring Quality with Evals
[`chapter8/`](chapter8/)

Builds a full RAG evaluation pipeline across two sub-projects:

| Sub-project | What it adds |
|-------------|-------------|
| `evals/` | RAG chatbot, data prep pipeline (3 steps), trace generator |
| `measuring_quality_with_evals/` | Qualitative eval with open and axial coding |

Demonstrates how to systematically measure and improve chatbot quality using grounded theory coding techniques.

### Chapter 10 — RAG Chatbot
[`chapter10/`](chapter10/)

A production-style RAG chatbot for GROSS software customer support. On each turn, it queries Pinecone for relevant documentation chunks, injects them into the system prompt, and enforces citation of sources. The model's internal `[[chunk-id]]` citations are stripped before displaying to the user.

### Chapter 11 — RAG Chatbot with Query Expansion
[`chapter11/`](chapter11/)

Extends chapter 10 with two pre-processing steps before each Pinecone search: **query expansion** rewrites the user's message into a more descriptive form, and **product classification** identifies which GROSS product is being asked about so a metadata filter can narrow the search to the relevant manual. Both steps use `gpt-4.1-nano` for speed and cost efficiency.

## Status

Work in progress — more chapters coming.
