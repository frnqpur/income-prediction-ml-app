# 11 Case Study EN — Income Prediction

## SEO Metadata

**Title:** Income Prediction Machine Learning Demo — Frengki Josua Purba Portfolio Project  
**Slug:** `/projects/income-prediction`  
**URL:** `frengkipurba.com/projects/income-prediction`  
**Meta description:** A machine learning case study for income category prediction using Python, scikit-learn, and Streamlit, including target leakage audit, valid pipeline design, model evaluation, and an interactive demo.

## Hero Section

# Income Prediction — Machine Learning Demo

A machine learning project for predicting whether a person's income category is `<=50K` or `>50K` based on selected demographic and work-related attributes. This project was refactored from an old academic notebook into a cleaner, more valid, recruiter-ready portfolio project.

**Tech stack:** Python, Pandas, Scikit-learn, Streamlit, Joblib, Jupyter Notebook

### CTA

- **Try Demo:** `[add Streamlit demo link]`
- **View Notebook HTML:** `/projects/income-prediction/notebook-html/income-prediction.html`
- **GitHub Repository:** `[add GitHub repository link]`
- **Screenshots:** `/projects/income-prediction/screenshots`

---

## 1. Project Background

This project started as an old academic notebook for income classification. The original goal was to predict whether an individual's income category was `<=50K` or `>50K`.

During the portfolio audit, I found that the original notebook was not ready to publish because it contained a serious **target leakage** issue. The old model achieved 100% accuracy, but the score was invalid because it used a `cluster` feature generated from the target column `Class`.

I refactored the project with the following goals:

- separate features and target correctly,
- remove leakage-causing features,
- build a safer preprocessing pipeline,
- evaluate the model against a baseline and relevant metrics,
- create an interactive demo that recruiters can try.

---

## 2. Problem Statement

The key question of this project is:

> How can we build a classification model that predicts whether a person's income category is `<=50K` or `>50K` using valid input features, without using the target or target-derived variables?

This project is not intended for real-world financial, hiring, credit, or high-stakes decision-making. It is designed as a machine learning portfolio demonstration.

---

## 3. Dataset

The project uses `adult_dataset.csv`, an income classification dataset with two target classes:

- `<=50K`
- `>50K`

Dataset size:

| Information | Value |
|---|---:|
| Rows | 32,561 |
| Original columns | 15 |
| Target | `Class` / `income` |

Target distribution:

| Target | Count | Percentage |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

The dataset is imbalanced, so the model should be evaluated against a majority-class baseline.

---

## 4. Feature Selection

Features used in the demo:

| Feature | Type | Reason for inclusion |
|---|---|---|
| `age` | Numeric | Basic demographic feature available in the dataset |
| `workclass` | Categorical | Employment category |
| `education` | Categorical | Education level |
| `education.num` | Numeric | Numeric education representation |
| `marital.status` | Categorical | Marital status |
| `occupation` | Categorical | Occupation type |
| `relationship` | Categorical | Household relationship |
| `capital.gain` | Numeric | Financial attribute in the dataset |
| `capital.loss` | Numeric | Financial attribute in the dataset |
| `hours.per.week` | Numeric | Weekly working hours |

Excluded features:

| Feature | Reason for exclusion |
|---|---|
| `Class` | Prediction target; must never be used as input |
| `cluster` | Generated from the target in the old notebook, causing leakage |
| `race` | Sensitive attribute, excluded from the public demo |
| `sex` | Sensitive attribute, excluded from the public demo |
| `fnlwgt` | Excluded to keep the demo form simple |
| `native.country` | Excluded to simplify input and reduce public demo complexity |

---

## 5. Methodology

The final demo pipeline follows these steps:

1. Load the dataset.
2. Rename the target column to `income`.
3. Replace `?` values with missing values.
4. Select valid demo features.
5. Split data into train and test sets with target stratification.
6. Impute missing values:
   - numeric features: median,
   - categorical features: most frequent value.
7. Apply one-hot encoding to categorical features.
8. Train a `GradientBoostingClassifier`.
9. Evaluate the model on the test set.
10. Save the complete pipeline with `joblib`.
11. Load the pipeline in a Streamlit app for interactive predictions.

---

## 6. Model Evaluation

Majority-class baseline:

```text
75.92%
```

Demo model results:

| Metric | Score |
|---|---:|
| Accuracy | 86.56% |
| F1-score for `>50K` | 68.63% |
| ROC-AUC for `>50K` | 92.08% |

Confusion matrix:

| Actual / Predicted | `<=50K` | `>50K` |
|---|---:|---:|
| `<=50K` | 7,020 | 397 |
| `>50K` | 916 | 1,436 |

Interpretation:

- The model outperforms the majority-class baseline.
- The 86.56% accuracy is more realistic than the old notebook's invalid 100% accuracy.
- The `>50K` class is harder to predict because it has fewer samples.
- F1-score for the minority class should be shown so recruiters can evaluate more than just accuracy.

---

## 7. Demo App

The demo app is built with Streamlit.

Prediction form inputs:

- age,
- workclass,
- education,
- education.num,
- marital.status,
- occupation,
- relationship,
- capital.gain,
- capital.loss,
- hours.per.week.

Displayed outputs:

- predicted income class,
- probability for each class,
- a note that the prediction is for portfolio demonstration only,
- a disclaimer that the model should not be used for real-world high-stakes decisions.

---

## 8. Limitations

Important limitations:

- The dataset is imbalanced.
- The dataset contains sensitive attributes.
- The public demo excludes `race` and `sex`.
- The model has not undergone a full fairness audit.
- The prediction should not be used for hiring, credit, financial, or high-stakes decisions.
- The model depends on historical data and may inherit bias from the source dataset.

---

## 9. What I Learned

Through this project, I learned that:

- old machine learning notebooks need to be audited critically before being published,
- high accuracy does not always mean a good model,
- target leakage can make evaluation look perfect while being invalid,
- a baseline is essential, especially for imbalanced datasets,
- preprocessing pipelines should be reproducible,
- portfolio demos should explain model outputs, limitations, and ethical considerations clearly.

---

## 10. Website Page Structure

Use the following structure for:

```text
frengkipurba.com/projects/income-prediction
```

### Section 1 — Hero

- Project title
- 2–3 sentence summary
- Tech stack
- CTA: Try Demo, View Notebook HTML, GitHub Repository, Screenshots

### Section 2 — Project Background

- Origin from an old academic notebook
- Why the project was refactored
- Main issue: target leakage

### Section 3 — Dataset

- Data size
- Target column
- Class distribution
- Example features

### Section 4 — Methodology

- Preprocessing
- Feature selection
- Model training
- Model persistence with `joblib`

### Section 5 — Evaluation

- Baseline
- Accuracy
- F1-score
- ROC-AUC
- Confusion matrix

### Section 6 — Demo

- Prediction form screenshot
- Prediction result screenshot
- Try Demo CTA

### Section 7 — Limitations

- Dataset bias
- Sensitive attributes
- Not for real-world high-stakes decisions

### Section 8 — What I Learned

- Technical lessons
- Model validation lessons
- Communication lessons

### Section 9 — Final CTA

- Try Demo
- View Notebook HTML
- GitHub Repository
- Screenshots

---

## 11. Suggested Portfolio Copy

**Short summary:**  
I refactored an old machine learning notebook into a more valid and recruiter-friendly Income Prediction demo. I identified target leakage that made the original 100% accuracy invalid, rebuilt the pipeline using valid input features, added realistic evaluation, and created a Streamlit demo.

**Role:** Data Science, Machine Learning, Streamlit Demo Development  
**Tools:** Python, Pandas, Scikit-learn, Streamlit, Joblib, Jupyter Notebook
