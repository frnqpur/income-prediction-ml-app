# Case Study ID — Income Prediction

## Meta SEO

**Title:** Income Prediction Machine Learning Demo — Portfolio Project Frengki Josua Purba  
**Slug:** `/projects/income-prediction`  
**URL:** `frengkipurba.com/projects/income-prediction`  
**Meta description:** Studi kasus machine learning untuk prediksi kategori pendapatan menggunakan Python, scikit-learn, dan Streamlit, lengkap dengan audit target leakage, pipeline valid, evaluasi model, dan demo interaktif.

## Hero Section

# Income Prediction — Machine Learning Demo

Project machine learning untuk memprediksi kategori pendapatan seseorang berdasarkan data demografis dan pekerjaan. Project ini dikembangkan ulang dari notebook kuliah lama menjadi portfolio project yang lebih rapi, valid, dan siap ditinjau recruiter.

**Tech stack:** Python, Pandas, Scikit-learn, Streamlit, Joblib, Jupyter Notebook

### CTA

- **Try Demo:** `[tambahkan link demo Streamlit]`
- **View Notebook HTML:** `/projects/income-prediction/notebook-html/income-prediction.html`
- **GitHub Repository:** `[tambahkan link GitHub]`
- **Screenshots:** `/projects/income-prediction/screenshots`

---

## 1. Latar Belakang Project

Project ini awalnya berasal dari notebook kuliah lama untuk klasifikasi pendapatan. Tujuan awalnya adalah memprediksi apakah income seseorang berada pada kategori `<=50K` atau `>50K`.

Saat diaudit ulang untuk kebutuhan portfolio, ditemukan bahwa notebook lama belum layak langsung dipublikasikan karena terdapat **target leakage**. Model lama mencapai accuracy 100%, tetapi skor tersebut tidak valid karena model memakai fitur `cluster` yang dibuat dari target `Class`.

Karena itu, project ini diperbaiki dengan fokus pada:

- memisahkan fitur dan target secara benar,
- menghapus fitur yang menyebabkan leakage,
- membuat preprocessing pipeline yang lebih aman,
- mengevaluasi model dengan baseline dan metrik yang lebih relevan,
- membuat demo interaktif agar recruiter bisa mencoba prediksi.

---

## 2. Problem Statement

Masalah yang ingin diselesaikan adalah:

> Bagaimana membangun model klasifikasi yang dapat memprediksi apakah pendapatan seseorang berada pada kategori `<=50K` atau `>50K` berdasarkan atribut input yang valid, tanpa menggunakan target atau fitur turunan target?

Project ini tidak dimaksudkan untuk pengambilan keputusan nyata dalam konteks finansial, pekerjaan, kredit, atau layanan penting. Project ini hanya digunakan sebagai demonstrasi portfolio machine learning.

---

## 3. Dataset

Dataset yang digunakan adalah `adult_dataset.csv`. Dataset berisi data populasi dengan target income:

- `<=50K`
- `>50K`

Ukuran dataset:

| Informasi | Nilai |
|---|---:|
| Jumlah baris | 32,561 |
| Jumlah kolom awal | 15 |
| Target | `Class` / `income` |

Distribusi target:

| Target | Jumlah | Persentase |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

Dataset tidak seimbang, sehingga model perlu dibandingkan dengan baseline majority class.

---

## 4. Feature Selection

Fitur yang digunakan dalam demo:

| Feature | Tipe | Alasan digunakan |
|---|---|---|
| `age` | Numeric | Fitur dasar demografis yang tersedia di dataset |
| `workclass` | Categorical | Informasi jenis pekerjaan |
| `education` | Categorical | Informasi pendidikan |
| `education.num` | Numeric | Representasi numerik tingkat pendidikan |
| `marital.status` | Categorical | Status pernikahan |
| `occupation` | Categorical | Jenis pekerjaan |
| `relationship` | Categorical | Relasi dalam keluarga |
| `capital.gain` | Numeric | Informasi finansial pada dataset |
| `capital.loss` | Numeric | Informasi finansial pada dataset |
| `hours.per.week` | Numeric | Jam kerja per minggu |

Fitur yang tidak digunakan:

| Feature | Alasan dikeluarkan |
|---|---|
| `Class` | Target prediksi, tidak boleh masuk sebagai input |
| `cluster` | Dibuat dari target pada notebook lama, menyebabkan leakage |
| `race` | Atribut sensitif, tidak dipakai pada demo publik |
| `sex` | Atribut sensitif, tidak dipakai pada demo publik |
| `fnlwgt` | Dikeluarkan agar form demo lebih sederhana |
| `native.country` | Dikeluarkan agar form demo lebih sederhana dan mengurangi kompleksitas input |

---

## 5. Methodology

Pipeline yang digunakan:

1. Load dataset.
2. Rename target menjadi `income`.
3. Replace nilai `?` menjadi missing value.
4. Pilih fitur valid untuk demo.
5. Split data menjadi train dan test dengan stratifikasi target.
6. Imputasi missing value:
   - numeric: median,
   - categorical: most frequent.
7. One-hot encoding untuk fitur kategorikal.
8. Train model `GradientBoostingClassifier`.
9. Evaluasi model pada test set.
10. Simpan pipeline dengan `joblib`.
11. Load pipeline di Streamlit app untuk demo interaktif.

---

## 6. Model Evaluation

Baseline majority class:

```text
75.92%
```

Hasil model demo:

| Metric | Score |
|---|---:|
| Accuracy | 86.56% |
| F1-score untuk kelas `>50K` | 68.63% |
| ROC-AUC untuk kelas `>50K` | 92.08% |

Confusion matrix:

| Actual / Predicted | `<=50K` | `>50K` |
|---|---:|---:|
| `<=50K` | 7,020 | 397 |
| `>50K` | 916 | 1,436 |

Interpretasi:

- Model mengungguli baseline majority class.
- Accuracy 86.56% lebih realistis dibanding accuracy 100% pada notebook lama.
- Kelas `>50K` masih lebih sulit diprediksi karena jumlah sampelnya lebih sedikit.
- F1-score kelas `>50K` perlu ditampilkan agar recruiter melihat performa minoritas, bukan hanya accuracy.

---

## 7. Demo App

Demo app dibuat menggunakan Streamlit.

Input form:

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

Output yang ditampilkan:

- predicted income class,
- probability untuk masing-masing kelas,
- catatan bahwa prediksi hanya untuk portfolio demonstration,
- disclaimer bahwa model tidak digunakan untuk keputusan nyata.

---

## 8. Limitations

Project ini memiliki batasan penting:

- Dataset tidak seimbang.
- Dataset memiliki atribut sensitif.
- Demo publik tidak memakai `race` dan `sex`.
- Model belum melalui fairness audit mendalam.
- Prediksi tidak boleh digunakan untuk keputusan hiring, kredit, atau finansial.
- Hasil model bergantung pada dataset historis dan dapat membawa bias dari data sumber.

---

## 9. What I Learned

Dari project ini saya belajar:

- audit project machine learning lama harus dilakukan secara kritis,
- accuracy tinggi tidak selalu berarti model bagus,
- target leakage dapat membuat evaluasi terlihat sempurna tetapi tidak valid,
- baseline sangat penting terutama pada dataset tidak seimbang,
- pipeline preprocessing perlu dibuat reproducible,
- demo portfolio harus menjelaskan model, batasan, dan interpretasi output secara jujur.

---

## 10. Struktur Halaman Website

Gunakan struktur berikut untuk halaman:

```text
frengkipurba.com/projects/income-prediction
```

### Section 1 — Hero

- Judul project
- Ringkasan 2–3 kalimat
- Tech stack
- CTA: Try Demo, View Notebook HTML, GitHub Repository, Screenshots

### Section 2 — Project Background

- Asal project dari notebook kuliah lama
- Alasan project diperbaiki
- Masalah utama: target leakage

### Section 3 — Dataset

- Jumlah data
- Target
- Distribusi kelas
- Contoh fitur

### Section 4 — Methodology

- Preprocessing
- Feature selection
- Model training
- Model persistence dengan `joblib`

### Section 5 — Evaluation

- Baseline
- Accuracy
- F1-score
- ROC-AUC
- Confusion matrix

### Section 6 — Demo

- Screenshot prediction form
- Screenshot prediction result
- CTA Try Demo

### Section 7 — Limitations

- Bias dataset
- Atribut sensitif
- Tidak untuk keputusan nyata

### Section 8 — What I Learned

- Pelajaran teknis
- Pelajaran validasi model
- Pelajaran komunikasi hasil model

### Section 9 — Final CTA

- Try Demo
- View Notebook HTML
- GitHub Repository
- Screenshots

---

## 11. Suggested Portfolio Copy

**Short summary:**  
Saya merefaktor notebook machine learning lama menjadi demo Income Prediction yang lebih valid dan recruiter-friendly. Saya menemukan target leakage yang membuat accuracy 100% tidak valid, lalu membangun ulang pipeline dengan fitur asli, preprocessing yang lebih aman, evaluasi realistis, dan demo Streamlit.

**Role:** Data Science, Machine Learning, Streamlit Demo Development  
**Tools:** Python, Pandas, Scikit-learn, Streamlit, Joblib, Jupyter Notebook
