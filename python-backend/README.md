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

## Smart Glasses Demo

```bash
uvicorn food_vision_backend.smart_glass_demo.api:app --reload
```

## Streamlit

### Development

```bash
poetry run streamlit run food_vision_backend/streamlit/app.py --server.headless true --server.runOnSave true
```

Open http://localhost:8501/.

## Eval
```bash
cd python-backend
python food_vision_backend/eval/compute_eval_statistics.py ../data/nutrition5k/nutrition5k_dataset-metadata-dish_metadata_cafe1.csv food_vision_backend/eval/res.csv food_vision_backend/eval/output_statistics.json
```