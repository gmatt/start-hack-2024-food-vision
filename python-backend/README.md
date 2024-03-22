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

## Streamlit

```bash
poetry run streamlit run food_vision_backend/streamlit/app.py --server.headless true --server.runOnSave true
```

Open http://localhost:8501/.

The main function is `predict_nutritions_form_image()` under `gpt4_vision` folder.

## Smart Glasses Demo

Currently, it works with Apple Vision, or with arbitrary smartphone.

Right now, only works on macOS, and uses screen sharing, which is hacky, and was
required because of the apple vision limitations.

On apple vision, a simple web view or web browser was used to display the UI.

After starting the backend and frontend, start screen sharing from the mobile device
to macOS for the app to work properly.

```bash
uvicorn food_vision_backend.smart_glass_demo.api:app --reload
```

For mobile, you can use ngrok to get https url, to get camera access.

If screen sharing is on, you can use the cell phone to simulate smart glasses and try
the app.

## Eval

To recalculate, download images, optionally adjust the 100 limit in download_images.py.
Then call generate_predictions(), then the command below.

```bash
python food_vision_backend/eval/compute_eval_statistics.py ../data/nutrition5k/nutrition5k_dataset-metadata-dish_metadata_cafe1.csv food_vision_backend/eval/res.csv food_vision_backend/eval/output_statistics.json
```

# Known issues

- Currently, in smart glasses demo, the photos used for image detection are not deleted, so the disk space can fill up
  quite fast.