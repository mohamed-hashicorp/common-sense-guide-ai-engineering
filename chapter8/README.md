# Chapter 8: Measuring Quality with Evals

This chapter demonstrates how to evaluate a RAG-based AI customer support chatbot using qualitative evaluation techniques (open coding and axial coding).

## Structure

```
chapter8/
├── evals/                        # RAG chatbot and data pipeline
└── measuring_quality_with_evals/ # Extended pipeline with qualitative eval
```

## Setup

A shared virtual environment is used across both directories.

```bash
cd chapter8
python -m venv .venv
source .venv/bin/activate
pip install openai pinecone-client python-dotenv docling
```

Both subdirectories require a `.env` file with the following keys:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Directories

### [`evals/`](evals/)

The core RAG chatbot with a data preparation pipeline and trace generator. Start here if you are new to the chapter.

### [`measuring_quality_with_evals/`](measuring_quality_with_evals/)

Extends the `evals/` pipeline with qualitative evaluation artifacts: manually coded chatbot responses (`open_coding.csv`) and a summary of failure themes (`axial_coding.csv`).
