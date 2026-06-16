# Income Prediction ML App — Deployment Guide

This guide explains how to deploy the Streamlit demo for the Income Prediction ML App.

Recommended platforms:

- Streamlit Community Cloud
- Hugging Face Spaces

Do **not** deploy this Python ML app to cPanel if your cPanel hosting does not support `pandas`, `scikit-learn`, `joblib`, or long-running Python apps.

---

## Final Repo Structure

Recommended GitHub structure:

```text
income-prediction-ml-app/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
├── sample_input.csv
├── artifacts/
│   ├── income_prediction_pipeline.joblib
│   ├── metrics.json
│   └── metadata.json
├── data/
│   ├── adult_dataset.csv
│   └── README.md
├── screenshots/
└── portfolio-kit/
```

The most important deployment files are:

```text
app.py
requirements.txt
artifacts/income_prediction_pipeline.joblib
artifacts/metrics.json
artifacts/metadata.json
```

---

## Safe requirements.txt

```text
streamlit>=1.32,<2.0
pandas>=2.0,<3.0
numpy>=1.24,<3.0
scikit-learn>=1.3,<2.0
joblib>=1.3,<2.0
```

This app does not need heavy notebook or visualization dependencies such as:

```text
jupyter
notebook
matplotlib
seaborn
missingno
tensorflow
torch
xgboost
```

---

## Local Test Command

From the local project directory:

```powershell
cd "E:\laragon\www\income-prediction-ml-app"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If the model artifact has a version mismatch, retrain it locally:

```powershell
python train_model.py
streamlit run app.py
```

---

## Connect to GitHub

Repository:

```text
https://github.com/frnqpur/income-prediction-ml-app
```

Typical update flow:

```powershell
cd "E:\laragon\www\income-prediction-ml-app"
git status
git add .
git commit -m "Update README and portfolio screenshots"
git push origin main
```

---

## Deploy to Streamlit Community Cloud

1. Open Streamlit Community Cloud.
2. Sign in with GitHub.
3. Select the repository:

```text
frnqpur/income-prediction-ml-app
```

4. Select branch:

```text
main
```

5. Set main file path:

```text
app.py
```

6. Deploy the app.

After deployment, test:

- homepage loads
- form input works
- prediction result appears
- confidence/probability appears
- model info appears
- metrics appear
- no missing artifact error

---

## Deploy to Hugging Face Spaces

1. Create a new Space.
2. Choose SDK:

```text
Streamlit
```

3. Upload or push the same repo files.
4. Keep `app.py` and `requirements.txt` at the root.
5. Ensure `artifacts/` is included.
6. Wait for the Space to build.

---

## Troubleshooting

### Model artifact could not be loaded

Possible cause:

```text
scikit-learn version mismatch
```

Fix:

```powershell
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

Then commit the regenerated `.joblib` if needed.

### FileNotFoundError for .joblib

Check that this file exists:

```text
artifacts/income_prediction_pipeline.joblib
```

### Metrics not showing

Check that this file exists:

```text
artifacts/metrics.json
```

### GitHub updated but Streamlit still shows old version

Try:

- reboot app from Streamlit dashboard
- clear cache
- check that Streamlit uses branch `main`
- check that main file path is `app.py`

---

## Final Sync Checklist

Before sharing the app to recruiters:

```text
[ ] Local app works.
[ ] GitHub repo has the latest app.py.
[ ] GitHub README shows all screenshots.
[ ] GitHub has artifacts folder.
[ ] Streamlit app is connected to the same GitHub repo.
[ ] Streamlit app uses branch main.
[ ] Streamlit main file path is app.py.
[ ] Live app visual matches local app.
[ ] README has the final live demo link.
```
