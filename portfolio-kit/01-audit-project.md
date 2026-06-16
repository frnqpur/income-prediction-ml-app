# 01 Audit Project — Predicting Income of a Population using Python

## Ringkasan audit

Project ini berisi project kuliah lama untuk prediksi kategori pendapatan populasi menggunakan Python. File utama yang diaudit adalah:

- `Project Big Data Frengki Josua Purba.ipynb`
- `adult_dataset.csv`
- `Readme/readme.md`
- folder `Readme/` berisi banyak gambar dokumentasi/screenshot

Status saat ini: **belum layak dipublikasikan sebagai ML project final tanpa perbaikan**, karena model akhir mengalami **data leakage berat**. Model mendapatkan akurasi 100%, tetapi bukan karena berhasil belajar pola dari fitur populasi, melainkan karena fitur input akhir (`cluster`) dibuat dari target (`Class`).

## Tujuan project

Berdasarkan notebook dan README, tujuan project adalah membuat model klasifikasi untuk memprediksi apakah pendapatan seseorang/populasi berada pada kategori:

- `<=50K`
- `>50K`

README menjelaskan bahwa project bertujuan:

1. membersihkan dan menyiapkan data,
2. membangun model Decision Tree,
3. mengevaluasi model,
4. mencoba tuning hyperparameter dengan GridSearchCV,
5. mengidentifikasi variabel yang memengaruhi pendapatan.

Catatan jujur: tujuan “mengidentifikasi variabel kunci” belum benar-benar tercapai pada source code final, karena fitur asli justru dibuang sebelum pemodelan akhir.

## Dataset

Dataset yang tersedia di project adalah file:

```text
adult_dataset.csv
```

Ukuran dataset berdasarkan file CSV:

- jumlah baris: `32,561`
- jumlah kolom: `15`
- target awal di CSV bernama `Unnamed: 14`
- setelah diproses di notebook, kolom target diganti nama menjadi `Class`

Kolom awal dataset:

| Kolom CSV | Nama setelah rename di notebook | Keterangan |
|---|---:|---|
| `age` | `A1` | usia |
| `workclass` | `A2` | kelas pekerjaan |
| `fnlwgt` | `A3` | final weight / bobot sampel |
| `education` | `A4` | pendidikan |
| `education.num` | `A5` | tingkat pendidikan numerik |
| `marital.status` | `A6` | status pernikahan |
| `occupation` | `A7` | pekerjaan |
| `relationship` | `A8` | hubungan keluarga |
| `race` | `A9` | ras |
| `sex` | `A10` | jenis kelamin |
| `capital.gain` | `A11` | capital gain |
| `capital.loss` | `A12` | capital loss |
| `hours.per.week` | `A13` | jam kerja per minggu |
| `native.country` | `A14` | negara asal |
| `Unnamed: 14` | `Class` | target pendapatan |

Distribusi target di file dataset:

| Class | Jumlah | Persentase |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

Catatan mismatch dengan README/notebook: README dan markdown notebook menyebut kelas “seimbang/balanced” atau “hampir seimbang”. Berdasarkan `value_counts()`, dataset **tidak seimbang** karena kelas `<=50K` sekitar 3.15 kali lebih banyak daripada kelas `>50K`.

## Target prediksi

Target prediksi adalah kolom:

```text
Class
```

Nilai target:

```text
<=50K
>50K
```

Di notebook, target kemudian diubah menjadi angka menggunakan `LabelEncoder`:

- `<=50K` menjadi `0`
- `>50K` menjadi `1`

## Fitur/input yang digunakan

Ada dua hal yang perlu dibedakan: **fitur yang tersedia di dataset** dan **fitur yang benar-benar dipakai model akhir**.

### Fitur yang tersedia di dataset

Dataset menyediakan 14 fitur kandidat:

```text
A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14
```

Fitur tersebut berasal dari kolom asli:

```text
age, workclass, fnlwgt, education, education.num, marital.status,
occupation, relationship, race, sex, capital.gain, capital.loss,
hours.per.week, native.country
```

### Fitur yang benar-benar digunakan model akhir

Model akhir **tidak memakai 14 fitur asli tersebut**.

Pada bagian pemodelan, notebook menjalankan kode berikut secara konseptual:

```python
selected_features = ['Class']
features = dataset[selected_features].copy()
features = pd.get_dummies(features)
dataset['cluster'] = kmeans.fit_predict(features)
```

Lalu sebelum training:

```python
columns_to_drop = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                   'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'Class']
X = dataset.drop(labels=columns_to_drop, axis=1)
y = dataset['Class']
```

Akibatnya, `X` hanya berisi satu kolom:

```text
cluster
```

Masalahnya, `cluster` dibuat dari `Class`. Jadi input model berasal langsung dari target. Ini adalah **data leakage**.

## Library Python

Library yang muncul di notebook:

| Library / modul | Status pemakaian di notebook |
|---|---|
| `pandas` | digunakan untuk load CSV, manipulasi dataframe, encoding sederhana |
| `numpy` | digunakan untuk `np.nan` dan operasi dasar |
| `seaborn` | digunakan untuk visualisasi countplot dan heatmap |
| `matplotlib.pyplot` | digunakan untuk plot |
| `missingno` | digunakan untuk visualisasi missing value |
| `sklearn.model_selection.train_test_split` | digunakan untuk split train-test |
| `sklearn.model_selection.GridSearchCV` | digunakan untuk hyperparameter tuning |
| `sklearn.tree.DecisionTreeClassifier` | model klasifikasi utama |
| `sklearn.metrics.classification_report` | evaluasi precision, recall, f1-score |
| `sklearn.metrics.confusion_matrix` | evaluasi confusion matrix |
| `sklearn.metrics.accuracy_score` | evaluasi accuracy |
| `sklearn.cluster.KMeans` | digunakan untuk membuat `cluster`, tetapi penggunaannya bermasalah karena berdasarkan target |
| `sklearn.preprocessing.LabelEncoder` | digunakan untuk encoding `Class` dan `cluster` |
| `IPython.display.Image` | visualisasi decision tree |
| `six.StringIO` | membantu export graphviz |
| `sklearn.tree.export_graphviz` | visualisasi tree |
| `pydot`, `graphviz`, `pydotplus` | visualisasi decision tree |

Library yang di-import tetapi tidak terlihat menjadi bagian penting pipeline akhir:

- `PCA`
- `Pipeline`
- `StandardScaler`
- `precision_score`
- `recall_score`
- `f1_score`

## Preprocessing

Tahapan preprocessing yang benar-benar ada di notebook:

1. Load dataset dari Google Drive path:

   ```python
   dataset = pd.read_csv('gdrive/My Drive/Pengantar Big Data/adult_dataset.csv')
   ```

   Catatan: path ini spesifik Google Colab/Google Drive dan belum portable untuk recruiter.

2. Rename semua kolom menjadi `A1` sampai `A14` dan `Class`.

3. Mengganti tanda `?` menjadi `NaN`:

   ```python
   dataset.replace("?", np.nan, inplace=True)
   ```

4. Missing value ditemukan pada:

   | Kolom | Missing setelah `?` menjadi `NaN` |
   |---|---:|
   | `A2` / `workclass` | 1,836 |
   | `A7` / `occupation` | 1,843 |
   | `A14` / `native.country` | 583 |

5. Manual mapping kategori ke angka untuk `A2`, `A4`, `A6`, `A7`, `A8`, `A9`, `A10`, dan `A14`.

6. Missing value diisi dengan median:

   ```python
   dataset['A2'] = dataset['A2'].fillna(dataset['A2'].median())
   dataset['A7'] = dataset['A7'].fillna(dataset['A7'].median())
   dataset['A14'] = dataset['A14'].fillna(dataset['A14'].median())
   ```

7. Beberapa kolom di-convert ke integer.

8. Kolom dengan satu nilai unik dihapus, tetapi pada dataset ini tidak ada kolom yang benar-benar terhapus karena jumlah kolom tetap 15.

9. Dibuat kolom `cluster` menggunakan KMeans dari `Class`.

10. Kolom object (`Class`, `cluster`) diubah menjadi angka menggunakan `LabelEncoder`.

11. Fitur asli `A1` sampai `A14` dan target `Class` di-drop dari `X`, sehingga model hanya memakai `cluster`.

### Catatan penting preprocessing

Ada bug mapping pada `A2`:

```python
A2 = {'Private': 1, 'State_gov': 2, 'Federal-gov': 3, ...}
```

Di dataset, nilai sebenarnya adalah:

```text
State-gov
```

bukan:

```text
State_gov
```

Karena typo ini, semua nilai `State-gov` tidak ter-map dan berubah menjadi `NaN`. Jumlah `State-gov` di dataset adalah `1,298` baris. Akibatnya missing value `A2` meningkat dari `1,836` menjadi `3,134` setelah mapping.

Selain itu, encoding kategori menggunakan angka manual dapat memberi kesan urutan palsu pada model Decision Tree. Untuk project portfolio, pendekatan yang lebih aman adalah memakai `OneHotEncoder` atau `OrdinalEncoder` yang didefinisikan secara eksplisit dalam pipeline.

## Model

Model yang digunakan:

```text
DecisionTreeClassifier
```

Model lain yang muncul:

```text
KMeans
```

Namun KMeans tidak digunakan sebagai model prediksi income yang valid. KMeans hanya digunakan untuk membuat kolom `cluster`, dan kolom ini dibuat dari target `Class`.

### Model default

Notebook membangun model:

```python
dt_default = DecisionTreeClassifier(max_depth=5)
dt_default.fit(X_train, y_train)
```

Karena `X_train` hanya berisi `cluster`, model mendapat pola yang bocor dari target.

### GridSearchCV

Notebook mencoba beberapa tuning:

- `max_depth`: `range(1, 40)`
- `min_samples_leaf`: `range(5, 200, 20)`
- `min_samples_split`: `range(5, 200, 20)`
- kombinasi final:

```python
param_grid = {
    'max_depth': range(5, 15, 5),
    'min_samples_leaf': range(50, 150, 50),
    'min_samples_split': range(50, 150, 50),
    'criterion': ["entropy", "gini"]
}
```

Hasil GridSearchCV yang tercetak:

```text
best accuracy 1.0
DecisionTreeClassifier(criterion='entropy', max_depth=5,
                       min_samples_leaf=50,
                       min_samples_split=50)
```

### Mismatch model optimal vs model final

Ada mismatch antara hasil GridSearchCV dan model yang dipakai setelahnya.

GridSearchCV menyatakan model terbaik:

```text
criterion='entropy', max_depth=5, min_samples_leaf=50, min_samples_split=50
```

Tetapi notebook kemudian membuat model:

```python
clf_gini = DecisionTreeClassifier(
    criterion="gini",
    random_state=100,
    max_depth=10,
    min_samples_leaf=50,
    min_samples_split=50
)
```

Lalu notebook juga membuat versi lain:

```python
clf_gini = DecisionTreeClassifier(
    criterion="gini",
    random_state=100,
    max_depth=3,
    min_samples_leaf=50,
    min_samples_split=50
)
```

Jadi klaim “model dengan hyperparameter optimal” belum konsisten dengan source code.

## Evaluasi

Split data yang digunakan:

```python
train_test_split(X, y, test_size=0.30, random_state=99)
```

Ukuran test set dari output evaluasi:

```text
9,769 baris
```

Hasil evaluasi yang tercetak di notebook:

```text
accuracy: 1.00
precision kelas 0: 1.00
recall kelas 0: 1.00
f1-score kelas 0: 1.00
precision kelas 1: 1.00
recall kelas 1: 1.00
f1-score kelas 1: 1.00
```

Confusion matrix:

```text
[[7475    0]
 [   0 2294]]
```

Catatan audit: hasil 100% ini **tidak boleh dipakai sebagai klaim performa model**, karena fitur `cluster` dibuat dari target `Class`. Evaluasi ini mengukur kebocoran target, bukan kemampuan model memprediksi income dari atribut populasi.

Sebagai pembanding, baseline sederhana dengan selalu menebak kelas mayoritas `<=50K` sudah mendapat sekitar `75.92%` accuracy pada dataset ini. Karena itu, setelah leakage diperbaiki, evaluasi sebaiknya membandingkan model terhadap baseline tersebut.

## Potensi data leakage / overfitting

### 1. Data leakage utama: `cluster` dibuat dari target

Ini masalah paling serius.

Notebook membuat `cluster` dari `Class`:

```python
selected_features = ['Class']
features = dataset[selected_features].copy()
features = pd.get_dummies(features)
dataset['cluster'] = kmeans.fit_predict(features)
```

Kemudian model memakai `cluster` sebagai satu-satunya fitur input. Karena `cluster` berasal dari `Class`, model seolah-olah sudah diberi jawaban.

Dampaknya:

- akurasi 100% tidak valid,
- confusion matrix sempurna tidak valid,
- classification report tidak valid,
- visualisasi tree tidak menunjukkan pola income yang sebenarnya,
- project belum bisa diklaim sebagai model prediksi income yang benar.

### 2. Preprocessing dilakukan sebelum train-test split

Median imputation dan encoding dilakukan sebelum `train_test_split`. Untuk project portfolio, preprocessing sebaiknya dimasukkan ke `Pipeline` dan di-fit hanya pada training set.

### 3. Mapping kategori manual berisiko

Kategori seperti pendidikan, pekerjaan, negara, ras, dan status pernikahan diberi angka manual. Untuk model tree, angka ini dapat menciptakan urutan yang tidak selalu bermakna.

### 4. Mismatch hasil tuning dan model final

Model terbaik dari GridSearchCV tidak sama dengan model final yang dipakai. Ini membuat dokumentasi performa sulit dipercaya.

### 5. Dataset tidak seimbang

Kelas `<=50K` jauh lebih banyak daripada `>50K`. Jika leakage diperbaiki, evaluasi perlu memakai metrik selain accuracy, seperti precision, recall, F1-score, ROC-AUC, dan confusion matrix.

### 6. Potensi bias dan fairness

Dataset memiliki atribut sensitif/protected seperti:

- `race`
- `sex`
- `native.country`

Kolom ini memang ada di file dataset, tetapi untuk portfolio sebaiknya diberi catatan etika: model tidak boleh digunakan untuk keputusan nyata yang berdampak pada akses finansial, pekerjaan, kredit, atau layanan penting tanpa audit fairness yang serius.

## Mismatch antara README dan source code

| Area | Klaim / dokumentasi | Kondisi di file/source code | Catatan audit |
|---|---|---|---|
| Distribusi kelas | README/notebook menyebut kelas seimbang/balanced atau hampir seimbang | `<=50K` = 24,720 dan `>50K` = 7,841 | Dataset tidak seimbang |
| Tujuan identifikasi variabel penting | README menyebut ingin melihat variabel yang memengaruhi income | Model akhir hanya memakai `cluster` | Variabel asli tidak dianalisis oleh model akhir |
| Model optimal | GridSearchCV menemukan `criterion='entropy', max_depth=5` | Model final memakai `gini`, `max_depth=10`, lalu `max_depth=3` | Tidak konsisten |
| Evaluasi 100% | Notebook menampilkan accuracy, precision, recall, F1 = 1.00 | Input model berasal dari target | Skor tidak valid karena leakage |
| Fitur prediksi | README menyebut atribut seperti usia, pekerjaan, status pernikahan, jenis kelamin, ras | Source code akhir membuang `A1` sampai `A14` | Model final tidak memakai fitur tersebut |
| Demo prediksi | Belum ada aplikasi demo | Hanya notebook Colab dan README | Perlu dibuat ulang sebagai app kecil |

## Pemeriksaan file sensitif

Saya tidak menemukan file seperti:

- `.env`
- credential/token/API key
- file private key
- database dump
- file log aplikasi
- file konfigurasi database

File yang ditemukan hanya:

- notebook `.ipynb`
- dataset `.csv`
- README markdown
- gambar-gambar untuk README

Catatan:

1. Notebook berisi path Google Drive:

   ```text
   gdrive/My Drive/Pengantar Big Data/adult_dataset.csv
   ```

   Ini bukan credential, tetapi tidak portable untuk recruiter.

2. README berisi link Google Drive dataset. Pastikan link tersebut memang boleh public sebelum repo dipublikasikan.

3. Dataset tidak berisi nama, email, nomor telepon, alamat, token, atau credential. Namun dataset berisi atribut demografis sensitif seperti `race`, `sex`, dan `native.country`, sehingga perlu catatan etika/fairness di README.

## Rekomendasi bentuk demo terbaik

Rekomendasi terbaik untuk recruiter: **Streamlit web app sederhana**.

Alasan:

- cocok untuk ML/data analysis portfolio,
- mudah dijalankan lokal,
- mudah dipublish ke Streamlit Community Cloud atau Hugging Face Spaces,
- recruiter bisa mencoba input dan melihat prediksi `<=50K` atau `>50K`,
- bisa menampilkan confidence/probability dan ringkasan model.

### Demo yang direkomendasikan

Buat demo dengan input dari fitur yang memang ada di dataset, misalnya:

- `age`
- `workclass`
- `education`
- `education.num`
- `marital.status`
- `occupation`
- `relationship`
- `capital.gain`
- `capital.loss`
- `hours.per.week`
- `native.country`

Untuk atribut sensitif:

- `race`
- `sex`

Sebaiknya diberi dua opsi:

1. model baseline tanpa atribut sensitif, atau
2. model dengan atribut sensitif tetapi disertai disclaimer fairness.

Untuk portfolio recruiter, opsi pertama lebih aman: **demo prediksi income tanpa `race` dan `sex`**, lalu jelaskan bahwa kolom tersebut tersedia di dataset tetapi sengaja tidak dipakai di demo untuk mengurangi risiko bias.

### Bentuk output demo

Output demo sebaiknya menampilkan:

- prediksi kelas: `<=50K` atau `>50K`,
- probabilitas prediksi jika model mendukung `predict_proba`,
- catatan bahwa hasil hanya untuk pembelajaran/portfolio,
- bukan untuk keputusan finansial atau employment decision nyata.

### Pipeline teknis yang disarankan

Untuk memperbaiki project sebelum dibuat demo:

1. Pisahkan `X` dan `y` dari data asli:

   ```python
   X = dataset.drop(columns=['Class'])
   y = dataset['Class']
   ```

2. Jangan membuat `cluster` dari `Class`.

3. Lakukan `train_test_split` sebelum fitting preprocessing.

4. Gunakan `ColumnTransformer`:

   - numeric: imputer median,
   - categorical: imputer most frequent + OneHotEncoder.

5. Gunakan `Pipeline`:

   ```text
   preprocessing -> model
   ```

6. Bandingkan beberapa model:

   - Logistic Regression,
   - Decision Tree,
   - Random Forest,
   - Gradient Boosting / XGBoost jika ingin lebih kuat.

7. Evaluasi dengan:

   - accuracy,
   - precision,
   - recall,
   - F1-score,
   - ROC-AUC,
   - confusion matrix,
   - baseline majority class.

8. Simpan model dengan `joblib`.

9. Buat `app.py` Streamlit untuk demo prediksi.

## Rekomendasi prioritas perbaikan sebelum repo public

### Prioritas 1 — wajib

- Hapus penggunaan `cluster` yang dibuat dari `Class`.
- Train model menggunakan fitur asli, bukan target turunan.
- Perbaiki split dan preprocessing dengan pipeline.
- Evaluasi ulang model dari nol.
- Revisi README agar tidak mengklaim akurasi 100% sebagai performa valid.

### Prioritas 2 — penting untuk portfolio

- Rename kolom `A1` sampai `A14` menjadi nama fitur asli agar lebih mudah dipahami recruiter.
- Tambahkan `requirements.txt`.
- Tambahkan struktur folder yang rapi, misalnya:

  ```text
  07_income-prediction/
  ├── app/
  │   └── app.py
  ├── data/
  │   └── adult_dataset.csv
  ├── notebooks/
  │   └── income_prediction_exploration.ipynb
  ├── src/
  │   ├── train.py
  │   └── predict.py
  ├── models/
  │   └── income_model.joblib
  ├── portfolio-content/
  │   └── 01-audit-project.md
  ├── README.md
  └── requirements.txt
  ```

### Prioritas 3 — nilai tambah

- Tambahkan model card singkat.
- Tambahkan fairness note karena dataset memakai atribut sensitif.
- Tambahkan screenshot demo.
- Tambahkan link demo Streamlit/Hugging Face Spaces.
- Tambahkan penjelasan business context yang lebih netral, misalnya “income classification for data analysis learning”, bukan klaim untuk keputusan bank nyata.

## Kesimpulan audit

Project ini punya bahan dasar yang baik untuk portfolio data science/ML karena sudah memiliki dataset, notebook eksplorasi, preprocessing awal, visualisasi, model Decision Tree, GridSearchCV, dan evaluasi.

Namun, versi saat ini belum siap dipublikasikan sebagai project prediksi income yang valid karena terjadi data leakage besar: fitur `cluster` dibuat dari target `Class`, lalu dipakai sebagai input tunggal model. Akurasi 100% harus dianggap tidak valid.

Arah terbaik adalah menjadikan project ini sebagai **Income Prediction ML App** dengan pipeline yang diperbaiki, evaluasi ulang tanpa leakage, dan demo Streamlit yang memungkinkan recruiter mencoba prediksi menggunakan input yang benar-benar berasal dari fitur dataset.
