# measuring_quality_with_evals

Extends the [`evals/`](../evals/) pipeline with a qualitative evaluation workflow using open coding and axial coding to identify failure patterns in the chatbot's responses.

## Files

| File | Purpose |
|---|---|
| `chatbot.py` | Interactive RAG chatbot |
| `trace_generator.py` | Runs all queries and saves chatbot responses to `traces.csv` |
| `rag_prep_step_1.py` | Downloads source PDFs and converts them to markdown |
| `rag_prep_step_2.py` | Cleans up markdown heading levels |
| `rag_prep_step_3.py` | Chunks markdown files and uploads them to Pinecone |
| `queries.csv` | Test questions used to generate traces |
| `traces.csv` | Generated chatbot responses (pre-populated) |
| `open_coding.csv` | Human-labeled evaluation of each chatbot response |
| `axial_coding.csv` | Failure themes grouped and counted from open coding |
| `data/` | Processed markdown files used for RAG retrieval |

## How the evaluation works

This directory demonstrates a qualitative approach to AI evaluation:

1. **Generate traces** — run `trace_generator.py` to produce a batch of chatbot responses for a fixed set of test queries.
2. **Open coding** — a human reads every response in `traces.csv` and writes a label: either `PASS` or a description of what went wrong. The results are saved in `open_coding.csv`.
3. **Axial coding** — the individual labels are grouped into recurring themes, summarized in `axial_coding.csv`.

This produces a ranked list of the chatbot's most common failure modes, which directly informs what to fix next.

### Failure themes found

| Failure | Count |
|---|---|
| Hallucinates | 8 |
| Answers before collecting enough info | 4 |
| Identifies app even though it's not clear from query | 3 |
| Refers to "documentation excerpts" | 2 |
| Sends user to external website | 1 |
| Provides irrelevant response | 1 |

## Prerequisites

Copy the `.env` file from the `evals/` directory or create one here:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

The Pinecone index `gross-app` must already exist. See [`evals/README.md`](../evals/README.md) for setup instructions.

## Running

### Upload data to Pinecone (first time only)

```bash
source ../.venv/bin/activate
python rag_prep_step_3.py
```

### Start the chatbot

```bash
source ../.venv/bin/activate
python chatbot.py
```

### Generate fresh traces

```bash
python trace_generator.py
```

The existing `traces.csv` and `open_coding.csv` were generated from a previous run and can be used as reference.
