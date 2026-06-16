# 06 Screenshot Checklist — Income Prediction

## Tujuan dokumen

Dokumen ini berisi checklist screenshot yang perlu disiapkan untuk project **Income Prediction** agar tampil rapi di GitHub, website portfolio, LinkedIn, dan CV.

Screenshot yang disarankan mencakup:

1. dataset preview;
2. preprocessing;
3. model evaluation;
4. prediction form;
5. prediction result;
6. folder/project structure jika diperlukan.

---

## 1. Folder penyimpanan screenshot

Simpan semua screenshot ke folder:

```text
07_income-prediction\demo-app\screenshots
```

Path lengkap di laptop:

```text
E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\demo-app\screenshots
```

Jika ingin memisahkan screenshot untuk website portfolio, boleh juga copy ke:

```text
07_income-prediction\portfolio-assets\screenshots
```

---

## 2. Format nama file screenshot

Gunakan nama file yang konsisten dan mudah dipahami:

```text
01-dataset-preview.png
02-preprocessing-summary.png
03-model-evaluation.png
04-prediction-form.png
05-prediction-result.png
06-demo-app-overview.png
07-notebook-html-preview.png
```

Format yang disarankan:

- `.png` untuk kualitas tajam;
- resolusi minimal 1280 px lebar;
- rasio 16:9 jika akan dipakai untuk video atau slide;
- hindari screenshot terlalu panjang yang sulit dibaca.

---

## 3. Checklist screenshot dataset

### File yang disarankan

```text
01-dataset-preview.png
```

### Ambil screenshot dari

Notebook HTML atau Jupyter Notebook pada bagian:

- `dataset.head()`;
- `dataset.shape`;
- daftar kolom;
- distribusi target income.

### Isi screenshot yang ideal

Screenshot sebaiknya memperlihatkan:

- beberapa baris awal dataset;
- jumlah baris dan kolom;
- target `<=50K` dan `>50K`;
- konteks bahwa dataset adalah Adult Income Dataset.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Dataset berisi data populasi dengan fitur seperti usia, pendidikan, pekerjaan, jam kerja per minggu, capital gain, capital loss, dan negara asal. Target prediksi adalah kategori income, yaitu `<=50K` atau `>50K`.

### Portfolio caption — English

The dataset contains population records with features such as age, education, occupation, weekly working hours, capital gain, capital loss, and native country. The prediction target is the income category: `<=50K` or `>50K`.

---

## 4. Checklist screenshot preprocessing

### File yang disarankan

```text
02-preprocessing-summary.png
```

### Ambil screenshot dari

Notebook pada bagian preprocessing atau script training yang menjelaskan:

- penggantian nilai `?` menjadi missing value;
- pemisahan fitur numerik dan kategorikal;
- imputasi missing value;
- one-hot encoding;
- train-test split;
- pipeline preprocessing.

### Isi screenshot yang ideal

Screenshot sebaiknya menunjukkan:

- daftar fitur yang dipakai;
- fitur yang tidak dipakai untuk demo, terutama `Class`, `cluster`, `race`, dan `sex`;
- pipeline preprocessing yang rapi;
- bukti bahwa preprocessing tidak memakai target sebagai fitur.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Tahap preprocessing membersihkan nilai tidak valid, menangani missing value, memisahkan fitur numerik dan kategorikal, serta menerapkan encoding pada fitur kategorikal. Demo tidak memakai target `Class`, fitur bocor `cluster`, maupun atribut sensitif seperti `race` dan `sex` sebagai input form.

### Portfolio caption — English

The preprocessing step handles invalid values, missing values, numerical and categorical features, and categorical encoding. The demo does not use the target column `Class`, the leaked `cluster` feature, or sensitive attributes such as `race` and `sex` as form inputs.

---

## 5. Checklist screenshot model evaluation

### File yang disarankan

```text
03-model-evaluation.png
```

### Ambil screenshot dari

Notebook final, terminal output `train_model.py`, atau Streamlit app pada bagian model performance.

### Isi screenshot yang ideal

Tampilkan metrik seperti:

- baseline accuracy;
- model accuracy;
- precision;
- recall;
- F1-score;
- ROC-AUC jika tersedia;
- confusion matrix jika visualnya jelas.

### Catatan penting

Jangan gunakan screenshot evaluasi notebook lama yang menunjukkan accuracy 100% sebagai hasil final. Skor tersebut tidak valid karena model lama memakai fitur `cluster` yang dibuat dari target `Class`.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Model dievaluasi menggunakan test set terpisah dan dibandingkan dengan baseline kelas mayoritas. Evaluasi tidak memakai fitur turunan target sehingga hasilnya lebih realistis untuk kebutuhan demo portfolio.

### Portfolio caption — English

The model is evaluated on a separate test set and compared against a majority-class baseline. The evaluation does not use target-derived features, making the result more realistic for a portfolio demo.

---

## 6. Checklist screenshot prediction form

### File yang disarankan

```text
04-prediction-form.png
```

### Ambil screenshot dari

Streamlit demo app setelah dijalankan:

```powershell
streamlit run app.py
```

Buka:

```text
http://localhost:8501
```

### Isi screenshot yang ideal

Prediction form sebaiknya menampilkan input:

- `age`;
- `workclass`;
- `education`;
- `education.num`;
- `marital.status`;
- `occupation`;
- `relationship`;
- `capital.gain`;
- `capital.loss`;
- `hours.per.week`;
- `native.country`.

### Input yang sengaja tidak ditampilkan

Untuk demo yang lebih aman, hindari form input berikut:

- `Class`, karena itu target;
- `cluster`, karena pada notebook lama dibuat dari target;
- `race`, karena atribut sensitif;
- `sex`, karena atribut sensitif.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Form prediksi dirancang agar recruiter dapat mencoba simulasi prediksi income menggunakan fitur yang valid dan relevan. Atribut sensitif tidak digunakan pada form demo untuk mengurangi risiko bias dan menjaga konteks etis project.

### Portfolio caption — English

The prediction form allows recruiters to test income prediction using valid and relevant features. Sensitive attributes are not included in the demo form to reduce bias risk and keep the project ethically scoped.

---

## 7. Checklist screenshot prediction result

### File yang disarankan

```text
05-prediction-result.png
```

### Ambil screenshot dari

Streamlit app setelah menekan tombol prediksi.

### Isi screenshot yang ideal

Tampilkan:

- input yang sudah diisi;
- hasil prediksi `<=50K` atau `>50K`;
- probabilitas/confidence jika tersedia;
- catatan bahwa prediksi hanya untuk demo portfolio;
- warning bahwa model tidak digunakan untuk keputusan nyata.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Output demo menampilkan kategori income yang diprediksi dan probabilitas model. Hasil ini hanya digunakan sebagai demonstrasi teknis, bukan untuk keputusan finansial, pekerjaan, kredit, atau layanan penting.

### Portfolio caption — English

The demo output shows the predicted income category and model probability. This result is intended only as a technical demonstration, not for real-world decisions related to finance, employment, credit, or essential services.

---

## 8. Checklist screenshot app overview

### File yang disarankan

```text
06-demo-app-overview.png
```

### Ambil screenshot dari

Halaman awal Streamlit app.

### Isi screenshot yang ideal

Tampilkan:

- judul app;
- deskripsi singkat project;
- sidebar input;
- bagian metrik model;
- tombol prediksi;
- catatan etika/fairness.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Demo app dibuat dengan Streamlit agar recruiter dapat mencoba model secara langsung melalui browser lokal. App menampilkan input form, hasil prediksi, metrik model, dan catatan penggunaan yang aman.

### Portfolio caption — English

The demo app is built with Streamlit so recruiters can try the model directly in a local browser. The app includes an input form, prediction output, model metrics, and safe-use notes.

---

## 9. Checklist screenshot notebook HTML

### File yang disarankan

```text
07-notebook-html-preview.png
```

### Ambil screenshot dari

File HTML final:

```text
07_income-prediction\notebook-html\income-prediction.html
```

Buka file tersebut di browser, lalu ambil screenshot bagian awal dan bagian evaluasi.

### Isi screenshot yang ideal

Tampilkan:

- judul notebook;
- project overview;
- bagian dataset atau evaluasi;
- layout HTML yang rapi.

### Narasi singkat untuk portfolio — Bahasa Indonesia

Notebook HTML digunakan sebagai dokumentasi lengkap proses analisis, mulai dari dataset, preprocessing, training model, evaluasi, sampai contoh prediksi.

### Portfolio caption — English

The HTML notebook serves as complete documentation of the analysis process, from dataset exploration and preprocessing to model training, evaluation, and prediction examples.

---

## 10. Cara mengambil screenshot di Windows

### Opsi 1 — Snipping Tool

1. Buka halaman yang ingin di-screenshot.
2. Tekan:

```text
Windows + Shift + S
```

3. Pilih area yang ingin diambil.
4. Simpan gambar sebagai `.png`.
5. Beri nama sesuai format checklist.

### Opsi 2 — Browser screenshot

Di Microsoft Edge atau Chrome:

1. Buka halaman Streamlit atau HTML notebook.
2. Tekan `F11` agar tampilan full screen.
3. Zoom ke 90% atau 100%.
4. Gunakan Snipping Tool.

### Opsi 3 — Screenshot full page

Jika ingin screenshot halaman panjang:

1. buka Chrome DevTools;
2. tekan `Ctrl + Shift + P`;
3. ketik `Capture full size screenshot`;
4. simpan hasilnya.

Gunakan full page screenshot hanya jika teks masih mudah dibaca.

---

## 11. Tips visual agar screenshot terlihat profesional

- Gunakan browser full screen.
- Tutup tab browser yang tidak relevan.
- Jangan tampilkan path pribadi jika tidak perlu.
- Gunakan zoom 90–100%.
- Pastikan teks tidak terlalu kecil.
- Gunakan data input yang wajar.
- Jangan tampilkan error di screenshot final.
- Jangan tampilkan akurasi 100% dari notebook lama sebagai hasil valid.
- Simpan screenshot dalam urutan cerita: dataset → preprocessing → evaluation → demo app → prediction result.

---

## 12. Screenshot minimal yang wajib ada

Jika waktu terbatas, cukup siapkan 4 screenshot utama:

```text
01-dataset-preview.png
02-preprocessing-summary.png
03-model-evaluation.png
04-prediction-form.png
```

Untuk portfolio yang lebih kuat, tambahkan:

```text
05-prediction-result.png
06-demo-app-overview.png
07-notebook-html-preview.png
```

---

## 13. Alternatif jika screenshot app belum siap

Jika demo interaktif belum siap, gunakan screenshot dari notebook final:

1. dataset preview;
2. preprocessing pipeline;
3. model evaluation;
4. contoh prediksi menggunakan dataframe sample.

Tambahkan caption bahwa interactive demo sedang disiapkan atau tersedia secara lokal.

### Bahasa Indonesia

Jika demo interaktif belum di-hosting, portfolio tetap dapat menampilkan notebook HTML, screenshot evaluasi, dan contoh prediksi. Ini sudah cukup untuk menunjukkan proses machine learning end-to-end secara teknis.

### English

If the interactive demo is not hosted yet, the portfolio can still present the HTML notebook, evaluation screenshots, and a sample prediction. This is enough to demonstrate an end-to-end machine learning workflow technically.

---

## 14. Checklist final screenshot

- [ ] `01-dataset-preview.png` sudah dibuat.
- [ ] `02-preprocessing-summary.png` sudah dibuat.
- [ ] `03-model-evaluation.png` sudah dibuat.
- [ ] `04-prediction-form.png` sudah dibuat.
- [ ] `05-prediction-result.png` sudah dibuat jika memungkinkan.
- [ ] Screenshot tidak menampilkan error.
- [ ] Screenshot tidak menampilkan credential, token, API key, atau data rahasia.
- [ ] Screenshot tidak mengklaim accuracy 100% dari model lama sebagai hasil valid.
- [ ] Screenshot tersimpan di folder `demo-app\screenshots`.
- [ ] Nama file sudah konsisten.

---

## 15. Kesimpulan

Screenshot untuk project Income Prediction sebaiknya membangun cerita yang jelas: dataset dipahami, preprocessing dilakukan dengan aman, model dievaluasi secara realistis, dan recruiter dapat mencoba prediksi melalui form demo. Fokus utama bukan membuat screenshot sebanyak mungkin, tetapi menunjukkan proses machine learning yang valid dan dapat dipercaya.
