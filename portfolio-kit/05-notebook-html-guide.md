# 05 Notebook HTML Guide — Income Prediction

## Tujuan dokumen

Dokumen ini menjelaskan cara mengekspor notebook project **Income Prediction** menjadi file HTML yang rapi untuk kebutuhan CV, GitHub, dan website portfolio.

File final yang disarankan:

```text
income-prediction.html
```

Folder penyimpanan final:

```text
07_income-prediction\notebook-html
```

Path lengkap di laptop:

```text
E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\notebook-html
```

---

## 1. Kenapa notebook perlu diekspor ke HTML?

Notebook HTML berguna agar recruiter bisa melihat hasil analisis tanpa harus membuka Jupyter Notebook atau menjalankan ulang kode.

HTML notebook cocok untuk ditampilkan sebagai:

- bukti proses data analysis;
- dokumentasi preprocessing;
- dokumentasi model training;
- dokumentasi evaluasi model;
- lampiran pada website portfolio;
- file preview untuk GitHub atau Google Drive.

Catatan penting: notebook lama memiliki masalah **target leakage** karena fitur `cluster` dibuat dari target `Class`. Jika notebook lama tetap diekspor, tambahkan catatan bahwa file tersebut adalah versi audit/legacy. Untuk portfolio final, ekspor notebook yang sudah diperbaiki dan tidak menggunakan `cluster` sebagai fitur prediksi.

---

## 2. Struktur folder yang disarankan

Sebelum export, siapkan struktur folder seperti ini:

```text
07_income-prediction/
├── source-code/
│   ├── Project Big Data Frengki Josua Purba.ipynb
│   ├── adult_dataset.csv
│   └── requirements.txt
├── notebook-html/
│   └── income-prediction.html
├── demo-app/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── artifacts/
└── portfolio-content/
    ├── 01-audit-project.md
    ├── 02-setup-guide.md
    ├── 03-model-review.md
    ├── 04-demo-app-plan.md
    ├── 05-notebook-html-guide.md
    ├── 06-screenshot-checklist.md
    └── 07-video-script.md
```

Buat folder `notebook-html` jika belum ada:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction"
mkdir notebook-html
```

---

## 3. Persiapan sebelum export

Masuk ke folder source code:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\source-code"
```

Aktifkan virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika virtual environment belum dibuat, gunakan panduan dari `02-setup-guide.md`.

Pastikan dependency notebook sudah terinstall:

```powershell
pip install -r requirements.txt
```

Cek apakah Jupyter tersedia:

```powershell
jupyter --version
```

---

## 4. Rapikan notebook sebelum export

Sebelum diekspor ke HTML, buka notebook dan lakukan hal berikut:

1. Pastikan dataset dibaca dari path lokal, bukan Google Drive Colab.
2. Restart kernel dan jalankan semua cell dari awal.
3. Hapus output error yang tidak perlu.
4. Tambahkan markdown explanation pada bagian penting.
5. Tambahkan catatan bahwa hasil notebook lama dengan accuracy 100% tidak valid jika masih memakai `cluster` dari target.
6. Pastikan grafik dan tabel evaluasi muncul dengan jelas.
7. Pastikan tidak ada token, credential, path private yang sensitif, atau informasi personal.

Kode dataset lokal yang disarankan:

```python
import pandas as pd

dataset = pd.read_csv('adult_dataset.csv')
dataset.head()
```

Untuk notebook final yang lebih valid, pastikan fitur tidak berisi target:

```python
assert 'Class' not in X.columns
assert 'cluster' not in X.columns
```

---

## 5. Cara export notebook ke HTML dari JupyterLab

Cara paling mudah:

1. Buka JupyterLab.
2. Buka notebook Income Prediction.
3. Pilih menu `File`.
4. Pilih `Save and Export Notebook As`.
5. Pilih `HTML`.
6. Simpan hasilnya sebagai:

```text
income-prediction.html
```

7. Pindahkan file HTML ke folder:

```text
07_income-prediction\notebook-html
```

---

## 6. Cara export notebook ke HTML dari terminal

Gunakan perintah berikut dari folder `source-code`:

```powershell
jupyter nbconvert --to html "Project Big Data Frengki Josua Purba.ipynb" --output "income-prediction.html"
```

Setelah berhasil, pindahkan file HTML ke folder final:

```powershell
move "income-prediction.html" "..\notebook-html\income-prediction.html"
```

Jika ingin menjalankan notebook sekaligus mengekspor output terbaru, gunakan:

```powershell
jupyter nbconvert --to html --execute "Project Big Data Frengki Josua Purba.ipynb" --output "income-prediction.html"
move "income-prediction.html" "..\notebook-html\income-prediction.html"
```

Catatan: opsi `--execute` akan menjalankan semua cell dari awal. Jika notebook lama masih memakai path Google Colab, export bisa gagal. Perbaiki path dataset terlebih dahulu.

---

## 7. Nama file final

Gunakan nama final berikut:

```text
income-prediction.html
```

Simpan di:

```text
07_income-prediction\notebook-html\income-prediction.html
```

Path lengkap:

```text
E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\notebook-html\income-prediction.html
```

---

## 8. Error umum saat export HTML

### Error: `jupyter is not recognized`

Penyebab: Jupyter belum terinstall atau virtual environment belum aktif.

Solusi:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Lalu coba ulang:

```powershell
jupyter --version
```

---

### Error: `ModuleNotFoundError`

Penyebab: package yang dipakai notebook belum terinstall di environment aktif.

Solusi:

```powershell
pip install -r requirements.txt
```

Jika error spesifik, misalnya `missingno`:

```powershell
pip install missingno
```

---

### Error: `FileNotFoundError: adult_dataset.csv`

Penyebab: path dataset tidak sesuai.

Solusi:

Pastikan `adult_dataset.csv` ada di folder yang sama dengan notebook, atau ubah kode menjadi:

```python
dataset = pd.read_csv('adult_dataset.csv')
```

Cek lokasi kerja notebook:

```python
import os
print(os.getcwd())
```

---

### Error: `google.colab` tidak ditemukan

Penyebab: notebook lama dibuat di Google Colab.

Solusi: comment atau hapus cell berikut:

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

Ganti dengan pembacaan dataset lokal:

```python
dataset = pd.read_csv('adult_dataset.csv')
```

---

### Error: export berhasil tetapi grafik tidak muncul

Penyebab umum:

- cell grafik belum dijalankan;
- output notebook belum tersimpan;
- backend plotting bermasalah.

Solusi:

1. Jalankan ulang semua cell.
2. Simpan notebook.
3. Export ulang.

Di notebook, gunakan:

```python
%matplotlib inline
```

---

## 9. Bagian notebook yang sebaiknya terlihat di HTML

Pastikan HTML final menampilkan bagian berikut:

### 9.1 Project overview

Berisi penjelasan singkat:

- project memprediksi income `<=50K` atau `>50K`;
- dataset menggunakan Adult Income Dataset;
- project digunakan untuk portfolio ML/data analysis;
- model demo menggunakan pipeline valid tanpa target leakage.

### 9.2 Dataset preview

Tampilkan:

- `dataset.head()`;
- `dataset.shape`;
- daftar kolom;
- distribusi target.

Contoh cell:

```python
print(dataset.shape)
display(dataset.head())
display(dataset['Class'].value_counts())
```

### 9.3 Missing value and preprocessing

Tampilkan:

- jumlah missing value;
- cara mengganti `?` menjadi missing value;
- fitur numerik dan kategorikal;
- strategi imputasi;
- encoding fitur kategorikal.

### 9.4 Model training

Tampilkan:

- model yang dipakai;
- alasan pemilihan model;
- train-test split;
- pipeline preprocessing + model.

### 9.5 Model evaluation

Tampilkan:

- baseline accuracy;
- model accuracy;
- confusion matrix;
- classification report;
- ROC-AUC jika tersedia;
- catatan bahwa evaluasi lama 100% tidak valid jika memakai target leakage.

### 9.6 Prediction example

Tampilkan contoh prediksi dari satu input dummy yang aman.

Contoh:

```python
sample_input = pd.DataFrame([{
    'age': 35,
    'workclass': 'Private',
    'education': 'Bachelors',
    'education.num': 13,
    'marital.status': 'Married-civ-spouse',
    'occupation': 'Prof-specialty',
    'relationship': 'Husband',
    'capital.gain': 0,
    'capital.loss': 0,
    'hours.per.week': 40,
    'native.country': 'United-States'
}])

prediction = model.predict(sample_input)
probability = model.predict_proba(sample_input)
print(prediction)
print(probability)
```

---

## 10. Catatan penting untuk recruiter

Tambahkan catatan ini di notebook final atau README:

### Bahasa Indonesia

Project ini adalah demo machine learning untuk kebutuhan portfolio. Model memprediksi kategori income berdasarkan fitur demografis dan pekerjaan dari dataset publik. Hasil prediksi tidak ditujukan untuk keputusan nyata terkait pekerjaan, kredit, pinjaman, asuransi, atau layanan penting lainnya. Versi demo menghindari penggunaan fitur sensitif seperti `race` dan `sex` pada form prediksi.

### English

This project is a machine learning demo for portfolio purposes. The model predicts income categories based on demographic and employment-related features from a public dataset. The prediction result is not intended for real-world decisions related to employment, credit, loans, insurance, or other high-impact services. The demo version avoids using sensitive attributes such as `race` and `sex` in the prediction form.

---

## 11. Checklist sebelum upload HTML ke portfolio

- [ ] File bernama `income-prediction.html`.
- [ ] File tersimpan di `07_income-prediction\notebook-html`.
- [ ] Notebook dapat dibuka di browser.
- [ ] Tidak ada cell error.
- [ ] Tidak ada path Google Drive yang masih aktif.
- [ ] Tidak ada credential, token, API key, atau file rahasia.
- [ ] Bagian dataset preview terlihat jelas.
- [ ] Bagian preprocessing terlihat jelas.
- [ ] Bagian model evaluation terlihat jelas.
- [ ] Jika notebook lama masih ditampilkan, ada catatan bahwa accuracy 100% tidak valid karena target leakage.
- [ ] Jika notebook final ditampilkan, model tidak memakai `Class` atau `cluster` sebagai fitur.

---

## 12. Kesimpulan

HTML notebook adalah bukti proses kerja yang penting untuk recruiter. File ini sebaiknya tidak hanya menampilkan kode, tetapi juga menjelaskan proses berpikir: mulai dari dataset, preprocessing, pemilihan model, evaluasi, keterbatasan model, sampai contoh prediksi.

Untuk project Income Prediction, hal paling penting adalah memastikan notebook HTML tidak mengklaim performa model lama yang bocor sebagai hasil final. Tampilkan versi yang sudah diperbaiki, atau beri label jelas bahwa notebook lama adalah legacy analysis yang sudah diaudit.
