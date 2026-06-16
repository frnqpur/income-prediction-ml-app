# 04 Demo App Plan — Income Prediction

## Ringkasan keputusan

Demo yang direkomendasikan untuk project **Income Prediction** adalah **Streamlit app**.

Alasan memilih Streamlit:

- cocok untuk demo machine learning sederhana;
- mudah dijalankan di laptop recruiter atau saat interview;
- form input dapat dibuat cepat tanpa frontend terpisah;
- bisa memuat model `.joblib`;
- mudah di-host ke Streamlit Community Cloud jika repo GitHub sudah rapi;
- lebih natural untuk portfolio data science dibanding membuat full-stack app dari nol.

Gradio juga bisa digunakan, tetapi untuk portfolio ini Streamlit lebih cocok karena bisa menampilkan form, metrik model, disclaimer, tabel input, dan penjelasan hasil prediksi dalam satu halaman yang mudah dibaca recruiter.

---

## Prinsip utama demo

Notebook lama tidak boleh langsung dijadikan dasar demo karena model lama mengalami **target leakage**. Kolom `cluster` dibuat dari target `Class`, lalu dipakai sebagai input model. Karena itu, accuracy 100% pada notebook lama tidak valid untuk diklaim.

Demo baru harus memakai pipeline valid:

```text
fitur asli yang aman -> preprocessing -> model -> evaluasi test set -> simpan model -> Streamlit prediction form
```

Kolom yang tidak boleh dipakai sebagai input:

```text
Class
cluster
```

Kolom yang sengaja tidak dipakai pada form demo publik:

```text
race
sex
native.country
fnlwgt
```

Alasan:

- `race` dan `sex` adalah atribut sensitif;
- `native.country` dapat menjadi proxy sensitif dan kurang nyaman untuk demo publik;
- `fnlwgt` valid secara dataset, tetapi sulit dipahami user umum dan tidak natural untuk form prediksi recruiter.

---

## Fitur input yang digunakan pada demo

Fitur yang direkomendasikan untuk model demo:

| Fitur | Tipe | Status | Alasan |
|---|---|---|---|
| `age` | numerik | digunakan | mudah dipahami dan valid dari dataset |
| `workclass` | kategorikal | digunakan | menjelaskan jenis pekerjaan umum |
| `education` | kategorikal | digunakan | mudah dipahami recruiter |
| `education.num` | numerik | digunakan, tetapi dihitung otomatis dari `education` | menghindari user mengisi dua informasi pendidikan yang saling bertentangan |
| `marital.status` | kategorikal | digunakan | fitur asli dataset |
| `occupation` | kategorikal | digunakan | fitur utama yang relevan untuk income |
| `relationship` | kategorikal | digunakan | fitur asli dataset |
| `capital.gain` | numerik | digunakan | fitur ekonomi dari dataset |
| `capital.loss` | numerik | digunakan | fitur ekonomi dari dataset |
| `hours.per.week` | numerik | digunakan | mudah dipahami dan relevan |

Input form minimal yang wajib terlihat:

```text
age
education
occupation
hours.per.week
```

Input tambahan yang masih valid:

```text
workclass
marital.status
relationship
capital.gain
capital.loss
```

---

## Model yang lebih layak untuk demo

Model yang direkomendasikan untuk draft demo adalah:

```text
GradientBoostingClassifier
```

Alasan:

- performanya biasanya lebih baik daripada Decision Tree tunggal;
- tetap tersedia langsung di `scikit-learn`;
- mendukung `predict_proba`, sehingga app bisa menampilkan probabilitas;
- tidak perlu dependency berat seperti XGBoost atau LightGBM;
- cukup ringan untuk demo lokal.

Model alternatif yang lebih sederhana:

```text
LogisticRegression
DecisionTreeClassifier
RandomForestClassifier
```

Untuk portfolio, pendekatan yang paling aman adalah menjelaskan bahwa model demo memakai pipeline baru, bukan model lama dari notebook yang mengalami leakage.

---

## Accuracy realistis

Berdasarkan dataset terlampir dan pipeline valid sederhana tanpa `race`, `sex`, `native.country`, `fnlwgt`, `Class`, dan `cluster`, baseline majority class berada di sekitar:

```text
75.92%
```

Dengan draft pipeline `GradientBoostingClassifier`, hasil realistis pada test split stratified dapat berada di sekitar:

```text
Accuracy sekitar 86%
ROC-AUC sekitar 0.92
F1-score kelas >50K sekitar 0.68
```

Angka ini jauh lebih masuk akal dibanding accuracy 100% dari notebook lama. Untuk README atau portfolio, tulis angka final hanya setelah Anda menjalankan ulang `train_model.py` di laptop dan menyimpan output metrics terbaru dari environment Anda sendiri.

---

## Struktur folder demo

Simpan file demo di folder:

```text
07_income-prediction\demo-app
```

Struktur yang disarankan:

```text
07_income-prediction/
├── demo-app/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .gitignore
│   ├── data/
│   │   ├── adult_dataset.csv
│   │   └── README.md
│   ├── artifacts/
│   │   ├── income_prediction_pipeline.joblib
│   │   ├── metrics.json
│   │   └── metadata.json
│   └── screenshots/
│       └── README.md
└── portfolio-content/
    └── 04-demo-app-plan.md
```

Catatan:

- `adult_dataset.csv` perlu Anda copy dari project lama ke folder `demo-app/data/`.
- Folder `artifacts/` akan berisi model hasil training.
- Folder `screenshots/` dipakai untuk menyimpan screenshot atau thumbnail demo.

---

## Cara save/load model dengan joblib

Training model dilakukan di `train_model.py`.

Alur training:

```text
load adult_dataset.csv
bersihkan ? menjadi missing value
rename target Unnamed: 14 menjadi income
pilih fitur aman
split train-test dengan stratify
fit preprocessing hanya pada train set
train GradientBoostingClassifier
ukur metrics pada test set
save pipeline ke artifacts/income_prediction_pipeline.joblib
save metrics ke artifacts/metrics.json
save metadata ke artifacts/metadata.json
```

Save model:

```python
joblib.dump(pipeline, "artifacts/income_prediction_pipeline.joblib")
```

Load model di Streamlit:

```python
pipeline = joblib.load("artifacts/income_prediction_pipeline.joblib")
```

Karena yang disimpan adalah full pipeline, file model sudah berisi:

- preprocessing numeric;
- preprocessing categorical;
- one-hot encoding;
- trained classifier.

Jadi `app.py` tidak perlu mengulang manual preprocessing.

---

## Cara menjalankan app di laptop

Masuk ke folder demo:

```powershell
cd "E:\Frengki Josua Purba\Job Seeker\Portfolio-Frengki\07_income-prediction\demo-app"
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

Copy dataset ke folder:

```text
07_income-prediction\demo-app\data\adult_dataset.csv
```

Train model:

```powershell
python train_model.py
```

Jalankan Streamlit:

```powershell
streamlit run app.py
```

Buka browser pada alamat yang muncul, biasanya:

```text
http://localhost:8501
```

---

## Form input pada app

Form input Streamlit sebaiknya berisi:

1. `age`
2. `workclass`
3. `education`
4. `marital.status`
5. `occupation`
6. `relationship`
7. `capital.gain`
8. `capital.loss`
9. `hours.per.week`

`education.num` tidak perlu diminta langsung dari user. Nilainya dihitung otomatis dari pilihan `education`.

Contoh:

| Education | education.num |
|---|---:|
| `HS-grad` | 9 |
| `Bachelors` | 13 |
| `Masters` | 14 |
| `Doctorate` | 16 |

---

## Output app yang perlu dijelaskan ke recruiter

Output app sebaiknya menampilkan:

1. **Prediksi kelas income**

   ```text
   <=50K
   >50K
   ```

2. **Probabilitas prediksi**

   Contoh:

   ```text
   Probability >50K: 68.4%
   ```

3. **Disclaimer**

   Jelaskan bahwa app hanya demo portfolio dan tidak boleh digunakan untuk keputusan nyata terkait pekerjaan, finansial, kredit, atau akses layanan.

4. **Model summary**

   Jelaskan bahwa model memakai pipeline valid tanpa target leakage.

5. **Metrics ringkas**

   Tampilkan accuracy, ROC-AUC, baseline accuracy, dan classification report ringkas dari `metrics.json`.

6. **Input yang digunakan**

   Tampilkan tabel input user agar recruiter memahami data yang dipakai untuk prediksi.

---

## Cara screenshot demo jika tidak dihosting

Jika app belum di-host, tetap buat bukti visual untuk portfolio.

Langkah screenshot:

1. Jalankan app:

   ```powershell
   streamlit run app.py
   ```

2. Isi form dengan contoh input yang masuk akal.
3. Klik tombol prediksi.
4. Ambil screenshot bagian:
   - judul app;
   - form input;
   - hasil prediksi;
   - metrics/model note.
5. Simpan ke folder:

   ```text
   07_income-prediction\demo-app\screenshots
   ```

Nama file yang disarankan:

```text
income-prediction-demo-home.png
income-prediction-demo-result.png
income-prediction-demo-metrics.png
```

Screenshot ini dapat dipakai di:

- README GitHub;
- website portfolio;
- LinkedIn post;
- CV project section.

---

## Cara rekam video demo jika tidak dihosting

Jika belum deploy, rekam video pendek 30–60 detik.

Isi video:

1. buka terminal dan jalankan `streamlit run app.py`;
2. buka app di browser;
3. ubah beberapa input form;
4. klik prediksi;
5. tunjukkan hasil prediksi dan probabilitas;
6. tunjukkan catatan bahwa model tidak memakai fitur sensitif dan tidak mengalami target leakage.

Tools yang bisa dipakai:

- Windows Snipping Tool dengan fitur screen recording;
- Xbox Game Bar (`Win + G`);
- OBS Studio jika ingin lebih rapi;
- Loom jika ingin link video online.

Nama file video yang disarankan:

```text
income-prediction-demo.mp4
```

Simpan ke:

```text
07_income-prediction\demo-app\screenshots
```

---

## Alternatif jika demo interaktif terlalu sulit

Jika Streamlit belum siap, gunakan alternatif berikut.

### Alternatif 1 — Notebook demo mode

Buat notebook baru:

```text
income_prediction_demo.ipynb
```

Isi notebook:

- load model `.joblib`;
- buat satu contoh input manual;
- tampilkan prediksi;
- tampilkan probabilitas;
- tampilkan metrics.

Kelemahannya: recruiter tidak bisa mencoba form interaktif.

### Alternatif 2 — CLI script

Buat file:

```text
predict_sample.py
```

Script menerima input hard-coded atau argumen terminal, lalu menampilkan prediksi.

Kelemahannya: kurang visual untuk recruiter non-teknis.

### Alternatif 3 — Static portfolio case study

Jika waktu sangat terbatas, tampilkan:

- screenshot notebook yang sudah diperbaiki;
- confusion matrix;
- metrics model valid;
- diagram pipeline;
- mockup form prediksi.

Kelemahannya: recruiter tidak bisa mencoba prediksi secara langsung.

### Alternatif 4 — Hosted notebook di Google Colab

Buat Colab yang bersih dan bisa dijalankan ulang dari awal. Simpan link di README.

Kelemahannya: kurang rapi dibanding Streamlit app, tetapi lebih cepat jika belum siap hosting.

---

## Checklist sebelum demo dipublikasikan

- [ ] Dataset sudah disimpan di `demo-app/data/adult_dataset.csv`.
- [ ] `train_model.py` berhasil dijalankan tanpa error.
- [ ] File `artifacts/income_prediction_pipeline.joblib` berhasil dibuat.
- [ ] File `artifacts/metrics.json` berhasil dibuat.
- [ ] `streamlit run app.py` berhasil membuka app.
- [ ] App tidak meminta input `race` dan `sex`.
- [ ] App tidak memakai `Class` atau `cluster` sebagai fitur.
- [ ] Hasil prediksi menampilkan kelas dan probabilitas.
- [ ] App menampilkan disclaimer bahwa prediksi hanya untuk demo portfolio.
- [ ] README menjelaskan bahwa angka 100% dari notebook lama tidak dipakai.
- [ ] Screenshot/video demo sudah disimpan.

---

## Narasi singkat untuk recruiter

Versi Bahasa Indonesia:

> Saya mengubah project kuliah lama menjadi demo machine learning yang lebih layak untuk portfolio. Pada audit awal, saya menemukan target leakage karena model lama memakai fitur yang dibuat dari target. Saya kemudian membuat pipeline baru dengan preprocessing yang valid, memilih fitur yang aman untuk form prediksi, menghindari atribut sensitif seperti race dan sex, menyimpan model dengan joblib, dan membuat demo Streamlit agar recruiter bisa mencoba prediksi income secara interaktif.

English version:

> I refactored an old academic machine learning project into a more portfolio-ready income prediction demo. During the initial audit, I found target leakage because the old model used a feature derived from the target variable. I rebuilt the pipeline with valid preprocessing, selected safer input features for the prediction form, excluded sensitive attributes such as race and sex, saved the model with joblib, and created a Streamlit demo so recruiters can interactively test income predictions.
