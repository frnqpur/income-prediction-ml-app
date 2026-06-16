# 07 Video Script — Income Prediction Demo

## Tujuan dokumen

Dokumen ini berisi script video demo 1–2 menit untuk project **Income Prediction**. Video ini dapat digunakan untuk:

- website portfolio;
- LinkedIn post;
- GitHub README;
- lampiran lamaran kerja;
- dokumentasi pribadi project.

Video sebaiknya singkat, jelas, dan fokus pada nilai teknis project: dataset, preprocessing, model evaluation, dan demo prediksi.

---

## 1. Durasi video yang disarankan

Durasi ideal:

```text
1–2 menit
```

Target durasi terbaik:

```text
90 detik
```

Struktur durasi:

| Bagian | Durasi |
|---|---:|
| Opening project | 10–15 detik |
| Dataset dan tujuan prediksi | 15–20 detik |
| Preprocessing dan validasi leakage | 20–25 detik |
| Evaluasi model | 15–20 detik |
| Demo prediction form | 20–30 detik |
| Closing | 10 detik |

---

## 2. File dan tampilan yang perlu disiapkan

Sebelum rekam video, siapkan:

1. browser membuka Streamlit app:

```text
http://localhost:8501
```

2. browser membuka HTML notebook:

```text
07_income-prediction\notebook-html\income-prediction.html
```

3. folder screenshot jika ingin menampilkan gambar pendukung:

```text
07_income-prediction\demo-app\screenshots
```

4. terminal sudah menjalankan app:

```powershell
streamlit run app.py
```

5. prediction form sudah siap diisi.

---

## 3. Cara rekam video di Windows

### Opsi 1 — Xbox Game Bar

1. Buka Streamlit app di browser.
2. Tekan:

```text
Windows + G
```

3. Klik tombol record.
4. Rekam demo 1–2 menit.
5. Simpan hasil rekaman.

### Opsi 2 — Microsoft Clipchamp

Gunakan Clipchamp untuk:

- memotong bagian awal/akhir video;
- menambahkan title singkat;
- menambahkan subtitle jika perlu;
- export ke MP4.

### Opsi 3 — OBS Studio

Gunakan OBS jika ingin hasil lebih profesional:

- scene: browser window;
- resolusi: 1920x1080;
- frame rate: 30 FPS;
- output: `.mp4`.

---

## 4. Tips rekaman agar profesional

- Gunakan layar 16:9.
- Tutup tab browser yang tidak relevan.
- Gunakan zoom browser 90–100%.
- Jangan tampilkan file pribadi, token, credential, atau path yang sensitif.
- Siapkan input demo sebelum mulai bicara.
- Jangan terlalu lama menjelaskan kode.
- Fokus pada alur: masalah → data → preprocessing → model → demo → hasil.
- Sebutkan bahwa demo tidak memakai fitur bocor `cluster` dan tidak memakai atribut sensitif seperti `race` dan `sex` pada form input.

---

## 5. Scene-by-scene video plan

### Scene 1 — Opening

Tampilan:

- halaman awal Streamlit app;
- judul project terlihat.

Pesan utama:

- project ini adalah demo machine learning untuk prediksi kategori income.

### Scene 2 — Dataset

Tampilan:

- screenshot atau HTML notebook bagian dataset preview.

Pesan utama:

- target adalah `<=50K` atau `>50K`;
- fitur berasal dari data demografis dan pekerjaan.

### Scene 3 — Preprocessing

Tampilan:

- notebook atau slide/screenshot preprocessing.

Pesan utama:

- missing value ditangani;
- fitur kategorikal di-encoding;
- target leakage dihindari.

### Scene 4 — Evaluation

Tampilan:

- metrik model di Streamlit atau notebook.

Pesan utama:

- model dibandingkan dengan baseline;
- hasil realistis lebih penting daripada angka sempurna yang tidak valid.

### Scene 5 — Prediction demo

Tampilan:

- form input Streamlit.

Pesan utama:

- recruiter bisa mengubah input dan mencoba prediksi.

### Scene 6 — Closing

Tampilan:

- hasil prediksi dan catatan penggunaan.

Pesan utama:

- project menunjukkan workflow ML end-to-end;
- hasil hanya untuk demo portfolio, bukan keputusan nyata.

---

# 6. Script video — Bahasa Indonesia

## Versi 60–90 detik

Halo, saya Frengki Josua Purba. Ini adalah demo project **Income Prediction**, yaitu aplikasi machine learning sederhana untuk memprediksi apakah income seseorang berada pada kategori `<=50K` atau `>50K`.

Dataset yang digunakan adalah Adult Income Dataset. Dataset ini memiliki fitur seperti usia, pendidikan, jenis pekerjaan, status pernikahan, jam kerja per minggu, capital gain, capital loss, dan negara asal. Target prediksinya adalah kategori income.

Pada project ini, saya melakukan preprocessing data, termasuk menangani nilai kosong, memisahkan fitur numerik dan kategorikal, serta menggunakan encoding untuk fitur kategorikal. Saya juga melakukan audit terhadap notebook lama dan menemukan bahwa hasil accuracy 100% tidak valid karena terdapat target leakage dari fitur `cluster` yang dibuat dari target `Class`.

Untuk demo ini, saya menggunakan pipeline yang lebih aman. Form prediksi tidak memakai target `Class`, tidak memakai fitur `cluster`, dan tidak memakai atribut sensitif seperti `race` dan `sex` sebagai input.

Di halaman demo, recruiter bisa mengisi input seperti age, education, occupation, hours per week, capital gain, capital loss, dan native country. Setelah tombol prediksi ditekan, aplikasi menampilkan kategori income yang diprediksi beserta probabilitas model.

Project ini saya siapkan sebagai portfolio machine learning end-to-end, mulai dari data preparation, model training, evaluation, hingga deployment demo sederhana menggunakan Streamlit. Hasil prediksi hanya untuk demonstrasi teknis dan tidak ditujukan untuk keputusan nyata seperti pekerjaan, kredit, atau layanan finansial.

---

## Versi 2 menit

Halo, saya Frengki Josua Purba. Pada video ini saya ingin memperkenalkan project **Income Prediction**, sebuah demo machine learning untuk memprediksi kategori income seseorang berdasarkan data populasi.

Project ini berasal dari project kuliah lama yang kemudian saya audit dan rapikan agar lebih layak ditampilkan sebagai portfolio. Tujuan utama project adalah membangun workflow machine learning yang dapat dipahami recruiter, mulai dari dataset, preprocessing, model training, evaluasi, sampai demo prediksi interaktif.

Dataset yang digunakan adalah Adult Income Dataset. Target prediksi terdiri dari dua kelas, yaitu `<=50K` dan `>50K`. Fitur yang digunakan mencakup usia, pendidikan, kelas pekerjaan, occupation, status pernikahan, relationship, jam kerja per minggu, capital gain, capital loss, dan native country.

Salah satu bagian penting dari project ini adalah review model secara kritis. Pada notebook lama, terdapat hasil accuracy 100%, tetapi setelah diaudit, hasil tersebut tidak valid karena ada target leakage. Fitur `cluster` dibuat dari target `Class`, lalu dipakai sebagai input model. Karena itu, model seolah-olah sudah mengetahui jawabannya.

Untuk versi demo, saya tidak menggunakan fitur tersebut. Pipeline yang lebih aman menggunakan fitur input asli, preprocessing untuk missing value, encoding fitur kategorikal, dan evaluasi pada test set terpisah. Saya juga tidak menampilkan atribut sensitif seperti `race` dan `sex` pada form prediksi agar demo lebih aman secara etis.

Di aplikasi Streamlit ini, recruiter dapat mencoba prediksi secara langsung. Input yang bisa diubah mencakup age, education, occupation, hours per week, capital gain, capital loss, dan beberapa fitur valid lainnya. Setelah input diisi, aplikasi akan menampilkan prediksi income dan probabilitas model.

Project ini menunjukkan kemampuan saya dalam data analysis, machine learning pipeline, model evaluation, debugging data leakage, dan membuat demo app sederhana. Namun, hasil prediksi tetap hanya untuk tujuan portfolio dan pembelajaran, bukan untuk keputusan nyata yang berdampak pada pekerjaan, kredit, atau layanan penting.

Terima kasih sudah melihat demo project ini.

---

# 7. Video script — English

## 60–90 second version

Hi, I’m Frengki Josua Purba. This is my **Income Prediction** project, a simple machine learning demo that predicts whether a person’s income category is `<=50K` or `>50K`.

The project uses the Adult Income Dataset. The dataset includes features such as age, education, occupation, marital status, weekly working hours, capital gain, capital loss, and native country. The prediction target is the income category.

In this project, I performed data preprocessing, including handling missing values, separating numerical and categorical features, and encoding categorical variables. I also audited the original notebook and found that the previous 100% accuracy result was not valid because of target leakage. The `cluster` feature was created from the target column `Class`, then used as a model input.

For this demo, I use a safer pipeline. The prediction form does not use the target column `Class`, does not use the leaked `cluster` feature, and does not include sensitive attributes such as `race` and `sex` as input fields.

In the demo app, recruiters can enter values such as age, education, occupation, weekly working hours, capital gain, capital loss, and native country. After clicking the prediction button, the app shows the predicted income category and the model probability.

This project demonstrates an end-to-end machine learning workflow, from data preparation and model training to evaluation and a simple Streamlit demo app. The prediction result is intended only for technical demonstration and is not meant for real-world decisions related to employment, credit, or financial services.

---

## 2-minute version

Hi, I’m Frengki Josua Purba. In this video, I will present my **Income Prediction** project, a machine learning demo that predicts a person’s income category based on population data.

This project started as an older university assignment, which I later audited and improved to make it more suitable for a professional portfolio. The main goal is to show a clear machine learning workflow that recruiters can understand, from dataset exploration and preprocessing to model training, evaluation, and an interactive prediction demo.

The dataset used in this project is the Adult Income Dataset. The target has two classes: `<=50K` and `>50K`. The features include age, education, workclass, occupation, marital status, relationship, weekly working hours, capital gain, capital loss, and native country.

One important part of this project is the critical model review. In the original notebook, the model achieved 100% accuracy. However, after auditing the code, I found that this result was not valid because of target leakage. The `cluster` feature was created from the target column `Class`, and then used as a model input. This means the model was indirectly given the answer.

For the demo version, I removed that leaked feature. The safer pipeline uses valid input features, preprocessing for missing values, categorical encoding, and evaluation on a separate test set. I also avoid using sensitive attributes such as `race` and `sex` in the prediction form to keep the demo more ethically scoped.

In this Streamlit app, recruiters can try the prediction directly. The input form includes age, education, occupation, weekly working hours, capital gain, capital loss, and other valid features. After submitting the form, the app displays the predicted income category and the model probability.

This project demonstrates my skills in data analysis, machine learning pipelines, model evaluation, detecting target leakage, and building a simple demo application. However, the prediction result is only for portfolio and learning purposes. It should not be used for real-world decisions that affect employment, credit, finance, or other high-impact services.

Thank you for watching this project demo.

---

## 8. Teks pembuka video

### Bahasa Indonesia

```text
Income Prediction — Machine Learning Demo
Predicting income category using a valid ML pipeline and Streamlit app.
```

### English

```text
Income Prediction — Machine Learning Demo
An end-to-end ML portfolio project with preprocessing, evaluation, and an interactive demo.
```

---

## 9. Teks penutup video

### Bahasa Indonesia

```text
Project highlights:
- Data preprocessing
- Target leakage review
- Model evaluation
- Streamlit prediction demo
- Ethical and safe-use notes
```

### English

```text
Project highlights:
- Data preprocessing
- Target leakage review
- Model evaluation
- Streamlit prediction demo
- Ethical and safe-use notes
```

---

## 10. Subtitle pendek untuk video

### Bahasa Indonesia

```text
Demo ini memprediksi kategori income berdasarkan fitur populasi dan pekerjaan. Model menggunakan pipeline yang lebih aman tanpa target leakage dan tanpa atribut sensitif pada form prediksi.
```

### English

```text
This demo predicts income categories using population and employment-related features. The model uses a safer pipeline without target leakage and without sensitive attributes in the prediction form.
```

---

## 11. Caption LinkedIn — Bahasa Indonesia

Saya menyiapkan ulang project **Income Prediction** sebagai portfolio machine learning.

Hal yang saya perbaiki dan dokumentasikan:

- audit model lama dan identifikasi target leakage;
- preprocessing data yang lebih aman;
- evaluasi model yang lebih realistis;
- demo prediksi menggunakan Streamlit;
- catatan etika karena dataset memiliki atribut sensitif.

Project ini menunjukkan workflow end-to-end mulai dari data preparation, model training, evaluation, hingga demo app sederhana untuk recruiter.

---

## 12. LinkedIn caption — English

I rebuilt my **Income Prediction** project as a machine learning portfolio project.

Key improvements and documentation:

- audited the original model and identified target leakage;
- improved the preprocessing workflow;
- used more realistic model evaluation;
- built a Streamlit prediction demo;
- added ethical notes because the dataset contains sensitive attributes.

This project demonstrates an end-to-end workflow from data preparation and model training to evaluation and a simple recruiter-friendly demo app.

---

## 13. Alternatif jika tidak ingin rekam suara

Jika tidak ingin menggunakan voice-over, buat video screen recording dengan teks overlay berikut:

1. `Income Prediction ML Demo`
2. `Dataset: Adult Income Dataset`
3. `Target: <=50K or >50K`
4. `Preprocessing: missing values, categorical encoding, train-test split`
5. `Critical review: removed target leakage from cluster feature`
6. `Demo form: valid non-sensitive input fields`
7. `Output: predicted income category and probability`
8. `For portfolio demonstration only`

Durasi tiap teks: 5–8 detik.

---

## 14. Alternatif jika demo interaktif terlalu sulit

Jika Streamlit app belum siap direkam, gunakan alur video berbasis notebook:

1. buka `income-prediction.html`;
2. tampilkan dataset preview;
3. tampilkan preprocessing;
4. tampilkan model evaluation;
5. tampilkan sample prediction di notebook;
6. tutup dengan rencana demo interaktif.

### Narasi Bahasa Indonesia

Jika demo interaktif belum tersedia, project tetap dapat ditampilkan melalui notebook HTML. Notebook menunjukkan proses machine learning end-to-end, mulai dari eksplorasi dataset, preprocessing, training model, evaluasi, dan contoh prediksi menggunakan input sample.

### English narration

If the interactive demo is not available yet, the project can still be presented through the HTML notebook. The notebook shows the end-to-end machine learning process, including dataset exploration, preprocessing, model training, evaluation, and a sample prediction.

---

## 15. Checklist sebelum upload video

- [ ] Durasi video 1–2 menit.
- [ ] Suara jelas jika memakai voice-over.
- [ ] Tidak ada tab browser pribadi.
- [ ] Tidak ada credential, token, API key, atau file rahasia.
- [ ] Tidak menampilkan klaim accuracy 100% sebagai hasil valid.
- [ ] Menjelaskan bahwa target leakage sudah diaudit.
- [ ] Menjelaskan bahwa demo tidak memakai `race` dan `sex` pada form input.
- [ ] Menjelaskan bahwa hasil hanya untuk portfolio demo.
- [ ] File video diekspor sebagai `.mp4`.
- [ ] Nama file video jelas, misalnya `income-prediction-demo.mp4`.

---

## 16. Nama file video yang disarankan

Gunakan nama:

```text
income-prediction-demo.mp4
```

Simpan ke folder:

```text
07_income-prediction\demo-app\video
```

atau:

```text
07_income-prediction\portfolio-assets\video
```

---

## 17. Kesimpulan

Video demo untuk project Income Prediction harus menampilkan kemampuan teknis secara singkat dan jujur. Fokus utama adalah menunjukkan bahwa project ini tidak hanya menjalankan model, tetapi juga mengaudit validitas model, menghindari target leakage, mengevaluasi performa secara realistis, dan menyediakan demo sederhana yang bisa dicoba recruiter.
