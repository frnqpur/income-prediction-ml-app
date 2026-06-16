# Income Prediction Streamlit Demo

Demo ini dibuat agar recruiter bisa mencoba prediksi income secara interaktif melalui form sederhana.

## Ringkasan

App ini menggunakan model baru yang lebih valid daripada notebook lama. Model lama di notebook tidak dipakai untuk demo karena terdapat target leakage: kolom `cluster` dibuat dari target `Class`, lalu digunakan sebagai fitur prediksi.

Demo ini tidak menggunakan:

```text
Class
cluster
race
sex
native.country
fnlwgt
```

Fitur yang digunakan:

```text
age
workclass
education
education.num
marital.status
occupation
relationship
capital.gain
capital.loss
hours.per.week
```

## Setup

Masuk ke folder demo:

```powershell
cd "E:\laragon\www\income-prediction-ml-app"
```

Buat virtual environment:

```powershell
py -3.10 -m venv .venv
```

Aktifkan virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependency:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Dataset

Copy file dataset lama ke:

```text
demo-app/data/adult_dataset.csv
```

Nama file harus:

```text
adult_dataset.csv
```

## Train model

Jalankan:

```powershell
python train_model.py
```

Output yang akan dibuat:

```text
artifacts/income_prediction_pipeline.joblib
artifacts/metrics.json
artifacts/metadata.json
```

## Jalankan app

```powershell
streamlit run app.py
```

Buka browser ke alamat yang muncul, biasanya:

```text
http://localhost:8501
```

## Catatan etika

Prediksi ini hanya untuk portfolio dan pembelajaran. Jangan gunakan model ini untuk keputusan nyata terkait pekerjaan, kredit, finansial, atau akses layanan.
