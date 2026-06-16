# Income Prediction Demo — Deployment Guide

## Overview

This folder contains a lightweight Streamlit demo for an Income Prediction machine learning project. The app predicts whether one person's income category is likely to be `<=50K` or `>50K` based on selected work, education, and weekly-hour attributes.

The demo uses a saved scikit-learn `.joblib` pipeline:

```text
artifacts/income_prediction_pipeline.joblib
```

The `.joblib` file stores the trained model pipeline, including preprocessing and the classifier. This lets the app run predictions without retraining every time.

## Files required for deployment

```text
app.py
requirements.txt
artifacts/income_prediction_pipeline.joblib
artifacts/metrics.json
artifacts/metadata.json
sample_input.csv
```

Optional for retraining:

```text
train_model.py
data/adult_dataset.csv
```

## Local setup

From this `demo-app` folder, create and activate a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the demo locally

```bash
streamlit run app.py
```

The app will open in your browser. Fill in the form for one person and click **Predict income**.

## Retrain the model if needed

Only retrain when the dataset, features, or model logic changes.

```bash
python train_model.py
```

This will regenerate:

```text
artifacts/income_prediction_pipeline.joblib
artifacts/metrics.json
artifacts/metadata.json
```

## Streamlit Community Cloud deployment

1. Push this folder to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Create a new app from the repository.
4. Set the app entry point to:

```text
app.py
```

If `app.py` is inside a subfolder, set the entry point to:

```text
demo-app/app.py
```

5. Make sure the `artifacts/` folder is included in the repository.
6. Deploy the app.

## Hugging Face Spaces deployment

1. Create a new Hugging Face Space.
2. Choose **Streamlit** as the SDK.
3. Upload or push the required files.
4. Make sure `app.py`, `requirements.txt`, and `artifacts/` are available at the Space root.
5. The Space will install dependencies and run the Streamlit app automatically.

## Recruiter demo checklist

Before sharing the link, confirm that:

- [ ] `streamlit run app.py` works locally.
- [ ] The form accepts one profile.
- [ ] Prediction result appears correctly.
- [ ] Confidence/probability appears when available.
- [ ] Model metrics load from `artifacts/metrics.json`.
- [ ] Model info loads from `artifacts/metadata.json`.
- [ ] Missing model or JSON files show graceful errors.
- [ ] The app does not expose sensitive data.
- [ ] The app does not claim leaked notebook accuracy.
- [ ] The README or portfolio case study explains that the old leakage issue was fixed.

## Notes for portfolio

This public demo intentionally excludes target-derived and sensitive columns such as `Class`, `cluster`, `race`, and `sex`. The goal is to show a clean portfolio-ready machine learning workflow, not to make real employment, credit, financial, or eligibility decisions.
