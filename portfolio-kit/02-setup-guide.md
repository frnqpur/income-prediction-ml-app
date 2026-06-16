# 02 Setup Guide — Income Prediction

## Tujuan dokumen

Dokumen ini menjelaskan cara menyiapkan environment lokal untuk menjalankan project **Income Prediction** dari notebook lama `Project Big Data Frengki Josua Purba.ipynb`.

Catatan penting: notebook lama masih mengandung masalah validitas model, terutama karena kolom `cluster` dibuat dari target `Class`, lalu dipakai sebagai fitur prediksi. Jadi setup ini hanya membantu menjalankan dan mereproduksi notebook. Untuk portfolio final, hasil model tetap harus diperbaiki dan divalidasi ulang.

---

## 1. Versi Python

Versi Python yang direkomendasikan:

```text
Python 3.10.x
```

Alasan:

- cukup stabil untuk `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, dan `missingno`;
- kompatibel dengan workflow notebook lama;
- mengurangi risiko error dependency saat menjalankan library visualisasi decision tree seperti `pydot`, `pydotplus`, dan `graphviz`.

Python 3.11 kemungkinan juga bisa digunakan, tetapi untuk portfolio yang mudah direproduksi recruiter, gunakan Python 3.10 terlebih dahulu.

Cek versi Python:

```bash
python --version
```

atau di Windows:

```bash
py --version
```

---

## 2. Struktur folder yang disarankan

Simpan file source code project di folder berikut:

```text
E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\source-code
```

Struktur minimal yang disarankan:

```text
07_income-prediction/
├── source-code/
│   ├── Project Big Data Frengki Josua Purba.ipynb
│   ├── adult_dataset.csv
│   └── requirements.txt
└── portfolio-content/
    ├── 01-audit-project.md
    └── 02-setup-guide.md
```

Jika nanti project sudah diperbaiki, struktur dapat diperluas menjadi:

```text
07_income-prediction/
├── source-code/
│   ├── notebooks/
│   ├── data/
│   ├── src/
│   ├── models/
│   ├── app/
│   └── requirements.txt
└── portfolio-content/
```

---

## 3. Membuat virtual environment

Buka PowerShell atau terminal, lalu masuk ke folder source code:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\source-code"
```

Buat virtual environment:

```powershell
py -3.10 -m venv .venv
```

Aktifkan virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika berhasil, terminal akan menampilkan prefix seperti:

```text
(.venv)
```

Jika aktivasi PowerShell ditolak, jalankan:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Lalu aktifkan ulang:

```powershell
.\.venv\Scripts\Activate.ps1
```

Untuk Command Prompt, gunakan:

```cmd
.venv\Scripts\activate.bat
```

---

## 4. Install requirements

Pastikan virtual environment sudah aktif, lalu upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Install dependency:

```powershell
pip install -r requirements.txt
```

Daftarkan kernel Jupyter agar mudah dipilih dari notebook:

```powershell
python -m ipykernel install --user --name income-prediction --display-name "Python (income-prediction)"
```

---

## 5. Isi `requirements.txt`

File `requirements.txt` disimpan di:

```text
07_income-prediction\source-code\requirements.txt
```

Isi file:

```txt
# Core data analysis
pandas>=2.0,<3.0
numpy>=1.24,<3.0

# Machine learning
scikit-learn>=1.3,<2.0
joblib>=1.3,<2.0

# Visualization
matplotlib>=3.7,<4.0
seaborn>=0.12,<1.0
missingno>=0.5,<1.0

# Notebook environment
jupyterlab>=4.0,<5.0
notebook>=7.0,<8.0
ipykernel>=6.0,<7.0

# Decision tree visualization
six>=1.16,<2.0
pydot>=2.0,<4.0
pydotplus>=2.0,<3.0
graphviz>=0.20,<1.0
```

Catatan: package Python `graphviz` berbeda dari aplikasi Graphviz di sistem operasi. Jika visualisasi decision tree gagal, install juga aplikasi Graphviz untuk Windows.

Cek apakah Graphviz tersedia:

```powershell
dot -V
```

Jika command tersebut tidak dikenali, install Graphviz melalui salah satu cara berikut:

```powershell
winget install Graphviz.Graphviz
```

atau install manual dari website resmi Graphviz, lalu tambahkan folder berikut ke `PATH` jika belum otomatis:

```text
C:\Program Files\Graphviz\bin
```

---

## 6. Cara menjalankan notebook

Masuk ke folder source code:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\source-code"
```

Aktifkan virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jalankan JupyterLab:

```powershell
jupyter lab
```

Buka notebook:

```text
Project Big Data Frengki Josua Purba.ipynb
```

Pilih kernel:

```text
Python (income-prediction)
```

Sebelum menjalankan semua cell, ubah path dataset dari format Google Drive/Colab menjadi path lokal.

Kode lama:

```python
dataset = pd.read_csv('gdrive/My Drive/Pengantar Big Data/adult_dataset.csv')
```

Kode lokal yang disarankan jika CSV berada satu folder dengan notebook:

```python
dataset = pd.read_csv('adult_dataset.csv')
```

Jika dataset disimpan di folder `data`, gunakan:

```python
dataset = pd.read_csv('data/adult_dataset.csv')
```

Untuk menjalankan notebook dari awal:

1. pilih menu `Kernel`;
2. pilih `Restart Kernel and Clear Outputs`;
3. pilih `Run All Cells`.

---

## 7. Error umum dan cara mengatasinya

### Error: `ModuleNotFoundError: No module named 'google.colab'`

Penyebab: notebook lama dibuat di Google Colab dan memiliki kode seperti:

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

Solusi lokal:

- hapus atau comment cell tersebut;
- gunakan path lokal untuk membaca dataset:

```python
dataset = pd.read_csv('adult_dataset.csv')
```

---

### Error: `FileNotFoundError: adult_dataset.csv`

Penyebab: file dataset tidak berada di folder yang sama dengan notebook, atau path CSV belum sesuai.

Solusi:

- pastikan `adult_dataset.csv` ada di folder `source-code`;
- atau sesuaikan path:

```python
dataset = pd.read_csv('data/adult_dataset.csv')
```

Cek working directory dari notebook:

```python
import os
print(os.getcwd())
```

---

### Error: `ModuleNotFoundError: No module named 'missingno'`

Penyebab: dependency belum terinstall.

Solusi:

```powershell
pip install -r requirements.txt
```

atau:

```powershell
pip install missingno
```

---

### Error: `ModuleNotFoundError: No module named 'pydotplus'`

Penyebab: library visualisasi decision tree belum terinstall.

Solusi:

```powershell
pip install pydot pydotplus graphviz
```

---

### Error: `GraphViz's executables not found` atau `dot not found`

Penyebab: package Python `graphviz` sudah terinstall, tetapi aplikasi Graphviz belum terinstall di Windows atau belum masuk `PATH`.

Solusi:

```powershell
winget install Graphviz.Graphviz
```

Setelah install, tutup dan buka ulang terminal, lalu cek:

```powershell
dot -V
```

Jika masih gagal, tambahkan folder berikut ke environment variable `PATH`:

```text
C:\Program Files\Graphviz\bin
```

---

### Error: virtual environment tidak aktif di PowerShell

Contoh error:

```text
running scripts is disabled on this system
```

Solusi:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Lalu aktifkan ulang environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### Error: kernel Jupyter tidak sesuai environment

Gejala:

- package sudah diinstall tetapi notebook tetap menampilkan `ModuleNotFoundError`;
- notebook memakai Python global, bukan `.venv`.

Solusi:

```powershell
python -m ipykernel install --user --name income-prediction --display-name "Python (income-prediction)"
```

Lalu di Jupyter pilih kernel:

```text
Python (income-prediction)
```

---

### Error: hasil notebook berbeda setelah package update

Penyebab umum:

- versi `scikit-learn` berbeda;
- `random_state` tidak diset;
- train-test split berbeda;
- urutan preprocessing berubah.

Solusi:

- gunakan `random_state` pada `train_test_split` dan model;
- catat versi package:

```python
import pandas as pd
import sklearn
import numpy as np

print('pandas:', pd.__version__)
print('scikit-learn:', sklearn.__version__)
print('numpy:', np.__version__)
```

---

## 8. Cara memastikan hasil notebook valid

Bagian ini penting karena notebook lama menghasilkan akurasi 100%, tetapi hasil tersebut tidak valid akibat data leakage.

### 8.1 Pastikan target tidak masuk ke fitur

Target prediksi adalah:

```text
Class
```

Fitur model tidak boleh berisi `Class` atau fitur turunan langsung dari `Class`.

Tambahkan cell validasi sebelum training:

```python
assert 'Class' not in X.columns, "Data leakage: kolom target Class masih ada di fitur X"
```

---

### 8.2 Jangan gunakan `cluster` yang dibuat dari `Class`

Pada notebook lama, `cluster` dibuat dari target:

```python
selected_features = ['Class']
features = dataset[selected_features].copy()
dataset['cluster'] = kmeans.fit_predict(features)
```

Kolom ini tidak boleh dipakai untuk training model prediksi income.

Tambahkan validasi:

```python
assert 'cluster' not in X.columns, "Data leakage: cluster dibuat dari target Class dan tidak boleh menjadi fitur"
```

Jika ingin memakai clustering, clustering harus dibuat dari fitur input asli, bukan dari target. Namun untuk versi portfolio awal, lebih baik hilangkan dulu kolom `cluster`.

---

### 8.3 Pastikan model memakai fitur asli

Model valid seharusnya memakai fitur seperti:

```text
age, workclass, fnlwgt, education, education.num, marital.status,
occupation, relationship, race, sex, capital.gain, capital.loss,
hours.per.week, native.country
```

atau nama sementara di notebook:

```text
A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14
```

Tambahkan validasi:

```python
print(X.columns.tolist())
assert X.shape[1] > 1, "Fitur terlalu sedikit. Pastikan model tidak hanya memakai cluster."
```

---

### 8.4 Lakukan split sebelum preprocessing yang belajar dari data

Untuk hasil yang lebih valid, operasi seperti imputasi median, imputasi kategori, scaling, dan encoding sebaiknya di-fit hanya pada training set.

Prinsip yang benar:

```text
train-test split -> fit preprocessing pada train -> transform train/test -> train model -> evaluasi test
```

Pendekatan yang disarankan adalah memakai `Pipeline` dan `ColumnTransformer` dari scikit-learn.

---

### 8.5 Bandingkan dengan baseline

Dataset ini tidak seimbang. Kelas mayoritas adalah `<=50K`, sekitar 75.92% dari data.

Artinya, model yang selalu menebak `<=50K` saja sudah mendapat accuracy sekitar 75.92%.

Tambahkan baseline:

```python
baseline_accuracy = y.value_counts(normalize=True).max()
print(f"Baseline majority-class accuracy: {baseline_accuracy:.4f}")
```

Model yang valid sebaiknya dibandingkan dengan baseline ini, bukan hanya dilihat dari accuracy mentah.

---

### 8.6 Jangan percaya akurasi 100% tanpa audit leakage

Jika hasil evaluasi menampilkan nilai seperti ini:

```text
accuracy = 1.00
precision = 1.00
recall = 1.00
f1-score = 1.00
```

maka lakukan pengecekan ulang. Untuk dataset income seperti ini, skor sempurna hampir pasti menunjukkan salah satu masalah berikut:

- target masuk ke fitur;
- fitur turunan target masuk ke fitur;
- preprocessing dilakukan dengan cara yang bocor;
- train dan test tidak benar-benar terpisah;
- evaluasi dilakukan pada data training, bukan test set.

---

### 8.7 Gunakan metrik evaluasi yang lengkap

Karena dataset tidak seimbang, jangan hanya memakai accuracy.

Gunakan:

```python
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
```

Perhatikan khususnya:

- precision untuk kelas `>50K`;
- recall untuk kelas `>50K`;
- F1-score tiap kelas;
- jumlah data pada masing-masing kelas di test set.

---

### 8.8 Gunakan split yang reproducible

Gunakan `random_state` dan sebaiknya `stratify=y`:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=99,
    stratify=y
)
```

Dengan `stratify=y`, distribusi kelas pada train dan test akan lebih stabil.

---

## 9. Checklist validasi sebelum project dipublikasikan

Sebelum repo GitHub dibuat public, pastikan checklist berikut terpenuhi:

- [ ] Notebook bisa dijalankan dari awal sampai akhir tanpa Google Colab path.
- [ ] `adult_dataset.csv` terbaca dari path lokal atau folder `data`.
- [ ] `requirements.txt` tersedia di folder `source-code`.
- [ ] Tidak ada `.env`, token, credential, API key, atau file private.
- [ ] Target `Class` tidak masuk ke fitur model.
- [ ] Kolom `cluster` dari target tidak dipakai sebagai fitur.
- [ ] Preprocessing dilakukan tanpa leakage.
- [ ] Evaluasi dilakukan pada test set.
- [ ] Accuracy dibandingkan dengan baseline majority class.
- [ ] Classification report dan confusion matrix ditampilkan.
- [ ] README menjelaskan bahwa dataset mengandung atribut sensitif seperti `race`, `sex`, dan `native.country`.
- [ ] Tidak ada klaim bahwa akurasi 100% adalah performa model valid.

---

## 10. Kesimpulan setup

Dengan setup ini, project Income Prediction dapat dijalankan secara lokal menggunakan virtual environment Python. Namun, tujuan utama setup bukan hanya membuat notebook berjalan, tetapi juga memastikan hasilnya dapat dipercaya.

Untuk portfolio final, langkah terpenting adalah memperbaiki pipeline machine learning agar model memprediksi income dari fitur populasi yang benar, bukan dari target atau fitur turunan target.
