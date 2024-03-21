# Food Vision Backend

# Requirements

Needs [Poetry](https://python-poetry.org).

# Initialize

```bash
cd python-backend
poetry install
```

Copy `.env.example` to `.env` and fill OpenAI API key.

https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key

# Run

## API

```bash
uvicorn food_vision_backend.api.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Streamlit

### Development

```bash
poetry run streamlit run food_vision_backend/streamlit/app.py --server.headless true --server.runOnSave true
```

Open http://localhost:8501/.
