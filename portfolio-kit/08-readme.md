# Income Prediction — README Draft

> Bilingual README draft for GitHub and portfolio use. Replace placeholder links before publishing.

---

## Bahasa Indonesia

# Income Prediction — Machine Learning Demo

Project ini adalah demo machine learning untuk memprediksi kategori pendapatan seseorang berdasarkan beberapa atribut demografis dan pekerjaan dari dataset Adult Income. Project ini dikembangkan ulang dari notebook kuliah lama agar lebih layak ditampilkan di CV, GitHub, dan website portfolio.

Versi awal notebook memiliki masalah **target leakage** karena model memakai fitur `cluster` yang dibuat dari target `Class`. Pada versi demo ini, pipeline diperbaiki agar model hanya memakai fitur input yang valid dan tidak memakai target atau fitur turunan target.

## CTA

- **Try Demo:** `[tambahkan link demo Streamlit]`
- **View Notebook HTML:** `notebook-html/income-prediction.html`
- **GitHub Repository:** `[tambahkan link repository]`
- **Screenshots:** `screenshots/`

## Project Overview

Project ini menunjukkan workflow dasar data science dan machine learning:

1. memahami struktur dataset,
2. membersihkan missing value,
3. memilih fitur yang aman untuk demo,
4. membangun preprocessing pipeline,
5. melatih model klasifikasi,
6. mengevaluasi model dengan metrik yang relevan,
7. menyajikan demo interaktif untuk recruiter.

## Dataset

Dataset yang digunakan adalah `adult_dataset.csv`, yaitu dataset income classification dengan target pendapatan:

- `<=50K`
- `>50K`

Dataset memiliki 32,561 baris dan 15 kolom pada file awal. Distribusi target tidak seimbang:

| Target | Jumlah | Persentase |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

Karena dataset tidak seimbang, accuracy tidak boleh menjadi satu-satunya metrik evaluasi.

## Valid Features for Demo

Form demo menggunakan fitur yang tersedia di dataset dan tidak dibuat dari target:

| Feature | Type | Keterangan |
|---|---|---|
| `age` | Numeric | Usia |
| `workclass` | Categorical | Kelas pekerjaan |
| `education` | Categorical | Pendidikan terakhir |
| `education.num` | Numeric | Tingkat pendidikan numerik |
| `marital.status` | Categorical | Status pernikahan |
| `occupation` | Categorical | Pekerjaan |
| `relationship` | Categorical | Relasi dalam keluarga |
| `capital.gain` | Numeric | Capital gain |
| `capital.loss` | Numeric | Capital loss |
| `hours.per.week` | Numeric | Jam kerja per minggu |

Fitur berikut sengaja tidak dipakai dalam demo:

- `Class`: target prediksi, tidak boleh menjadi input model.
- `cluster`: fitur dari notebook lama yang dibuat dari target, menyebabkan leakage.
- `race` dan `sex`: dikeluarkan dari form demo untuk mengurangi risiko bias pada demo publik.
- `fnlwgt` dan `native.country`: dikeluarkan dari demo sederhana agar input lebih mudah dipahami recruiter.

## Methodology

Pipeline demo menggunakan pendekatan berikut:

1. rename target menjadi `income`,
2. pisahkan fitur dan target,
3. split data dengan `train_test_split`, `test_size=0.30`, `random_state=99`, dan stratifikasi target,
4. imputasi missing value,
5. one-hot encoding untuk fitur kategorikal,
6. training model dengan `GradientBoostingClassifier`,
7. menyimpan pipeline menggunakan `joblib`,
8. load model di Streamlit app untuk prediksi interaktif.

## Model

Model demo menggunakan:

```text
GradientBoostingClassifier
```

Model ini dipilih karena cukup kuat untuk data tabular, tetap tersedia di `scikit-learn`, dan tidak membutuhkan dependency eksternal seperti XGBoost atau LightGBM.

## Evaluation

Hasil evaluasi demo app yang diretrain dari dataset:

| Metric | Score |
|---|---:|
| Baseline majority-class accuracy | 75.92% |
| Model accuracy | 86.56% |
| F1-score untuk kelas `>50K` | 68.63% |
| ROC-AUC untuk kelas `>50K` | 92.08% |

Confusion matrix:

| Actual / Predicted | `<=50K` | `>50K` |
|---|---:|---:|
| `<=50K` | 7,020 | 397 |
| `>50K` | 916 | 1,436 |

Interpretasi:

- Model lebih baik daripada baseline majority class.
- Model cukup baik mengenali kelas `<=50K`.
- Kelas `>50K` lebih sulit diprediksi karena jumlah datanya lebih sedikit.
- Hasil ini jauh lebih realistis dibanding accuracy 100% dari notebook lama yang terkena target leakage.

## Limitations

Project ini memiliki beberapa batasan:

- Dataset tidak seimbang.
- Dataset mengandung atribut sensitif seperti `race`, `sex`, dan `native.country`.
- Demo publik tidak memakai `race` dan `sex` untuk mengurangi risiko bias.
- Prediksi hanya untuk keperluan pembelajaran dan portfolio, bukan untuk keputusan finansial, hiring, kredit, atau layanan penting.
- Model belum melalui fairness audit yang mendalam.
- Model tidak boleh dinilai dari accuracy saja; precision, recall, F1-score, ROC-AUC, dan confusion matrix tetap perlu diperhatikan.

## What I Learned

Dari project ini, saya belajar:

- cara mengaudit notebook machine learning lama secara kritis,
- pentingnya mencegah target leakage,
- pentingnya membandingkan model dengan baseline,
- cara membangun preprocessing pipeline yang lebih aman,
- cara menyimpan dan memuat model dengan `joblib`,
- cara membuat demo ML sederhana dengan Streamlit,
- cara menjelaskan keterbatasan model kepada recruiter secara jujur.

## How to Run Locally

Masuk ke folder demo app:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\demo-app"
```

Buat virtual environment:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependency:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Train ulang model:

```powershell
python train_model.py
```

Jalankan Streamlit app:

```powershell
streamlit run app.py
```

Buka browser:

```text
http://localhost:8501
```

## Suggested Website Page Structure

Untuk halaman portfolio:

```text
frengkipurba.com/projects/income-prediction
```

Struktur halaman yang disarankan:

1. Hero section: judul, ringkasan project, CTA.
2. Project background: mengapa project ini dibuat ulang.
3. Dataset overview: sumber data, target, fitur, distribusi kelas.
4. Methodology: preprocessing, pipeline, model, deployment demo.
5. Evaluation: baseline, accuracy, F1-score, ROC-AUC, confusion matrix.
6. Interactive demo: tombol Try Demo atau embedded screenshot.
7. Limitations: leakage lama, bias dataset, scope penggunaan.
8. What I learned: insight teknis dan refleksi engineering.
9. Screenshots: notebook, evaluation, prediction form, prediction result.
10. Final CTA: Try Demo, View Notebook HTML, GitHub Repository, Screenshots.

---

## English

# Income Prediction — Machine Learning Demo

This project is a machine learning demo for predicting whether a person's income category is `<=50K` or `>50K` based on selected demographic and work-related attributes from the Adult Income dataset. It was refactored from an old academic notebook into a more recruiter-friendly portfolio project.

The original notebook had a serious **target leakage** issue because the model used a `cluster` feature generated from the target column `Class`. In this demo version, the pipeline is rebuilt so the model uses only valid input features and does not use the target or any target-derived feature.

## CTA

- **Try Demo:** `[add Streamlit demo link]`
- **View Notebook HTML:** `notebook-html/income-prediction.html`
- **GitHub Repository:** `[add repository link]`
- **Screenshots:** `screenshots/`

## Project Overview

This project demonstrates an end-to-end data science and machine learning workflow:

1. understanding the dataset structure,
2. handling missing values,
3. selecting safe features for a public demo,
4. building a preprocessing pipeline,
5. training a classification model,
6. evaluating the model with relevant metrics,
7. presenting an interactive demo for recruiters.

## Dataset

The project uses `adult_dataset.csv`, an income classification dataset with two target classes:

- `<=50K`
- `>50K`

The original dataset contains 32,561 rows and 15 columns. The target distribution is imbalanced:

| Target | Count | Percentage |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

Because the dataset is imbalanced, accuracy should not be used as the only evaluation metric.

## Valid Features for the Demo

The demo form uses features that exist in the dataset and are not derived from the target:

| Feature | Type | Description |
|---|---|---|
| `age` | Numeric | Age |
| `workclass` | Categorical | Work class |
| `education` | Categorical | Education level |
| `education.num` | Numeric | Numeric education level |
| `marital.status` | Categorical | Marital status |
| `occupation` | Categorical | Occupation |
| `relationship` | Categorical | Household relationship |
| `capital.gain` | Numeric | Capital gain |
| `capital.loss` | Numeric | Capital loss |
| `hours.per.week` | Numeric | Working hours per week |

The following fields are intentionally excluded from the demo:

- `Class`: the prediction target, therefore it must not be used as an input.
- `cluster`: a feature from the old notebook generated from the target, causing leakage.
- `race` and `sex`: excluded from the public demo form to reduce bias risk.
- `fnlwgt` and `native.country`: excluded to keep the demo form simple and recruiter-friendly.

## Methodology

The demo pipeline follows these steps:

1. rename the target column to `income`,
2. split features and target,
3. use `train_test_split` with `test_size=0.30`, `random_state=99`, and target stratification,
4. impute missing values,
5. apply one-hot encoding to categorical features,
6. train a `GradientBoostingClassifier`,
7. save the trained pipeline with `joblib`,
8. load the model in a Streamlit app for interactive prediction.

## Model

The demo uses:

```text
GradientBoostingClassifier
```

This model was selected because it performs well on tabular datasets, is available directly in `scikit-learn`, and does not require external dependencies such as XGBoost or LightGBM.

## Evaluation

Evaluation results from the retrained demo pipeline:

| Metric | Score |
|---|---:|
| Baseline majority-class accuracy | 75.92% |
| Model accuracy | 86.56% |
| F1-score for `>50K` | 68.63% |
| ROC-AUC for `>50K` | 92.08% |

Confusion matrix:

| Actual / Predicted | `<=50K` | `>50K` |
|---|---:|---:|
| `<=50K` | 7,020 | 397 |
| `>50K` | 916 | 1,436 |

Interpretation:

- The model performs better than the majority-class baseline.
- It identifies the `<=50K` class more reliably.
- The `>50K` class is harder to predict because it has fewer samples.
- These results are more realistic than the old notebook's 100% accuracy, which was caused by target leakage.

## Limitations

This project has several limitations:

- The dataset is imbalanced.
- The dataset contains sensitive attributes such as `race`, `sex`, and `native.country`.
- The public demo excludes `race` and `sex` to reduce bias risk.
- Predictions are for learning and portfolio demonstration only, not for financial, hiring, credit, or high-stakes decisions.
- The model has not undergone a complete fairness audit.
- The model should not be judged by accuracy alone; precision, recall, F1-score, ROC-AUC, and the confusion matrix should also be reviewed.

## What I Learned

Through this project, I learned how to:

- critically audit an old machine learning notebook,
- identify and remove target leakage,
- compare model performance against a baseline,
- build a safer preprocessing pipeline,
- save and load a model with `joblib`,
- create a simple ML demo with Streamlit,
- communicate model limitations honestly to recruiters.

## How to Run Locally

Go to the demo app folder:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\demo-app"
```

Create and activate a virtual environment:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Retrain the model:

```powershell
python train_model.py
```

Run the Streamlit app:

```powershell
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## Suggested Website Page Structure

Recommended portfolio page URL:

```text
frengkipurba.com/projects/income-prediction
```

Suggested sections:

1. Hero section: title, summary, CTA.
2. Project background: why the project was refactored.
3. Dataset overview: data source, target, features, class distribution.
4. Methodology: preprocessing, pipeline, model, demo deployment.
5. Evaluation: baseline, accuracy, F1-score, ROC-AUC, confusion matrix.
6. Interactive demo: Try Demo button or demo screenshots.
7. Limitations: old leakage issue, dataset bias, usage scope.
8. What I learned: technical insights and engineering reflection.
9. Screenshots: notebook, evaluation, prediction form, prediction result.
10. Final CTA: Try Demo, View Notebook HTML, GitHub Repository, Screenshots.
