# evals

A RAG-based AI customer support chatbot for fictional software products made by the company GROSS, along with a data preparation pipeline and trace generator.

## Products

| Product | Type |
|---|---|
| Flamehamster | Web browser |
| Rumblechirp | Email client |
| GuineaPigment | SVG drawing tool |
| EMRgency | Electronic medical record system |
| Verbiage++ | Content management system |

## Files

| File | Purpose |
|---|---|
| `chatbot.py` | Interactive RAG chatbot (run this to chat) |
| `trace_generator.py` | Runs all queries from `queries.csv` through the chatbot and saves results to `traces.csv` |
| `rag_prep_step_1.py` | Downloads source PDFs and converts them to markdown |
| `rag_prep_step_2.py` | Cleans up markdown heading levels |
| `rag_prep_step_3.py` | Chunks markdown files and uploads them to Pinecone |
| `queries.csv` | Test questions used to generate traces |
| `traces.csv` | Generated chatbot responses for each query |
| `data/` | Processed markdown files used for RAG retrieval |

## Prerequisites

Copy the `.env` file from the parent directory or create one here:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Running

### First-time setup

The `data/` folder is already populated so steps 1 and 2 can be skipped. You only need to create the Pinecone index and upload the data once.

**Create the Pinecone index:**

```python
import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
pc.create_index_for_model(
    name="gross-app",
    cloud="aws",
    region="us-east-1",
    embed={"model": "llama-text-embed-v2", "field_map": {"text": "chunk_text"}}
)
```

**Upload data to Pinecone:**

```bash
source ../.venv/bin/activate
python rag_prep_step_3.py
```

> Note: This takes several minutes due to rate limit pauses between batches.

### Start the chatbot

```bash
source ../.venv/bin/activate
python chatbot.py
```

Type your question at the `User:` prompt. Type `exit` to quit.

### Generate traces

```bash
python trace_generator.py
```

Reads all 23 queries from `queries.csv`, runs each through the chatbot, and writes results to `traces.csv`.
