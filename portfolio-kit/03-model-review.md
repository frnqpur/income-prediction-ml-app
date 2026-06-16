# 03 Model Review — Income Prediction

## Ringkasan review

Project **Income Prediction** memiliki ide portfolio yang bagus karena topiknya mudah dipahami recruiter: membuat model machine learning untuk memprediksi apakah income seseorang berada pada kategori `<=50K` atau `>50K` berdasarkan atribut demografis dan pekerjaan.

Namun, model pada notebook lama **belum valid untuk diklaim sebagai model prediksi income**, karena terjadi **target leakage** yang sangat serius. Model akhir tidak benar-benar belajar dari fitur seperti usia, pekerjaan, pendidikan, jam kerja, atau capital gain/loss. Model justru memakai kolom `cluster` yang dibuat dari target `Class`, sehingga hasil accuracy 100% tidak dapat dipercaya.

Kesimpulan utama:

- notebook lama boleh disimpan sebagai arsip pembelajaran;
- model lama tidak boleh dipakai sebagai klaim performa portfolio;
- project harus diperbaiki dengan pipeline baru yang memakai fitur asli;
- demo recruiter sebaiknya memakai model valid sederhana, bukan model 100% dari notebook lama;
- form prediksi harus menghindari input sensitif seperti `race`, `sex`, dan sebaiknya `native.country`.

---

## 1. Target prediksi

Target yang benar adalah kolom:

```text
Class
```

Target berasal dari kolom CSV:

```text
Unnamed: 14
```

Nilai target:

```text
<=50K
>50K
```

Dalam notebook, target kemudian diubah menjadi numerik dengan `LabelEncoder`, sehingga secara praktis menjadi:

```text
0 = <=50K
1 = >50K
```

Target ini valid untuk binary classification.

---

## 2. Fitur valid

Dataset memiliki 14 fitur kandidat sebelum target:

| Kolom asli | Nama di notebook | Status untuk model | Catatan |
|---|---:|---|---|
| `age` | `A1` | valid | numerik, mudah dipahami recruiter |
| `workclass` | `A2` | valid | kategorikal |
| `fnlwgt` | `A3` | valid secara dataset, kurang ideal untuk form demo | sulit dipahami user umum; bisa dipakai di training, tetapi tidak wajib ditampilkan di form demo |
| `education` | `A4` | valid | kategorikal |
| `education.num` | `A5` | valid | numerik; hati-hati karena mirip informasi `education` |
| `marital.status` | `A6` | valid | kategorikal |
| `occupation` | `A7` | valid | kategorikal |
| `relationship` | `A8` | valid | kategorikal |
| `race` | `A9` | sensitif | sebaiknya tidak dipakai di demo portfolio |
| `sex` | `A10` | sensitif | sebaiknya tidak dipakai di demo portfolio |
| `capital.gain` | `A11` | valid | numerik |
| `capital.loss` | `A12` | valid | numerik |
| `hours.per.week` | `A13` | valid | numerik, mudah dipahami |
| `native.country` | `A14` | sensitif/kontekstual | sebaiknya tidak dipakai di form demo publik |

### Rekomendasi fitur untuk model portfolio

Untuk model portfolio yang aman dan mudah dijelaskan, gunakan fitur berikut:

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

Fitur berikut sebaiknya tidak dimasukkan ke form demo publik:

```text
race
sex
native.country
```

Fitur berikut boleh dipertimbangkan untuk dikeluarkan dari form demo karena kurang intuitif untuk user:

```text
fnlwgt
```

Jika `fnlwgt` tetap dipakai dalam training, jelaskan bahwa itu adalah sample weight/estimation weight dari dataset, bukan input yang natural bagi user. Untuk demo recruiter, lebih baik training ulang model tanpa `fnlwgt` agar form lebih masuk akal.

---

## 3. Fitur tidak valid

Fitur berikut tidak boleh dipakai untuk prediksi:

```text
Class
cluster
```

Alasan:

- `Class` adalah target, bukan fitur;
- `cluster` pada notebook lama dibuat dari `Class`, sehingga merupakan turunan langsung dari target;
- memakai `cluster` berarti model diberi informasi jawaban secara tidak langsung.

Kode bermasalah di notebook:

```python
selected_features = ['Class']
features = dataset[selected_features].copy()
dataset['cluster'] = kmeans.fit_predict(features)
```

Kemudian notebook membuat `X` dengan membuang semua fitur asli dan target:

```python
columns_to_drop = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                   'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'Class']
X = dataset.drop(labels=columns_to_drop, axis=1)
y = dataset['Class']
```

Akibatnya `X` hanya berisi:

```text
cluster
```

Ini adalah sumber utama hasil 100% accuracy yang tidak valid.

---

## 4. Target leakage

### Temuan utama

Model lama mengalami **target leakage** karena fitur prediksi dibuat dari target.

Alur leakage di notebook:

1. Target asli adalah `Class`.
2. Notebook membuat fitur baru `cluster` dari `Class`.
3. Semua fitur asli `A1` sampai `A14` dibuang.
4. Model dilatih hanya dengan `cluster`.
5. Model menghasilkan accuracy 100%.

Secara logika, model tidak sedang memprediksi income dari data populasi. Model hanya membaca sinyal yang berasal dari target income itu sendiri.

### Dampak target leakage

Dampaknya sangat besar:

- accuracy 100% tidak valid;
- confusion matrix sempurna tidak valid;
- classification report 1.00 tidak valid;
- GridSearchCV juga tidak valid karena memakai fitur yang sudah bocor;
- model tidak layak dijadikan demo prediksi income;
- recruiter yang memahami machine learning dapat melihat ini sebagai red flag.

### Cara memperbaiki

Gunakan fitur asli sebagai `X` dan target sebagai `y`:

```python
X = dataset.drop(columns=['Class'])
y = dataset['Class']
```

Jika memakai nama kolom asli:

```python
X = df.drop(columns=['Unnamed: 14'])
y = df['Unnamed: 14']
```

Jangan membuat fitur apa pun dari target sebelum training.

---

## 5. Evaluasi model lama

Notebook lama menampilkan hasil evaluasi:

```text
accuracy = 1.00
precision = 1.00
recall = 1.00
f1-score = 1.00
```

Confusion matrix:

```text
[[7475    0]
 [   0 2294]]
```

Secara tampilan, hasil ini terlihat sempurna. Namun, hasil tersebut tidak boleh dipakai karena model memakai `cluster` yang dibuat dari `Class`.

Evaluasi yang benar harus dilakukan setelah:

1. target dipisahkan dari fitur;
2. fitur turunan target dihapus;
3. data dibagi menjadi train dan test set;
4. preprocessing di-fit hanya pada train set;
5. model dievaluasi pada test set;
6. hasil dibandingkan dengan baseline.

---

## 6. Accuracy realistis

Dataset tidak seimbang. Distribusi target pada file `adult_dataset.csv` adalah:

| Kelas | Jumlah | Persentase |
|---|---:|---:|
| `<=50K` | 24,720 | 75.92% |
| `>50K` | 7,841 | 24.08% |

Artinya, model dummy yang selalu menebak `<=50K` sudah mendapat accuracy sekitar:

```text
75.92%
```

Jadi, accuracy valid harus dibandingkan dengan baseline 75.92%, bukan dengan angka 100% dari notebook lama.

### Estimasi ulang berbasis dataset terlampir

Untuk memberi gambaran realistis, dilakukan simulasi ulang sederhana menggunakan dataset terlampir, tanpa `Class` dan tanpa `cluster` sebagai fitur. Pipeline valid memakai:

- train-test split 70:30;
- `stratify=y`;
- imputasi median untuk numerik;
- imputasi most frequent untuk kategorikal;
- OneHotEncoder untuk kategorikal;
- evaluasi pada test set.

Hasil pendekatan sederhana dengan semua fitur asli:

| Model valid sederhana | Accuracy | Precision `>50K` | Recall `>50K` | F1 `>50K` | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Decision Tree `max_depth=5` | 84.84% | 76.57% | 53.36% | 62.89% | 88.40% |
| Decision Tree `max_depth=8`, `min_samples_leaf=50` | 85.15% | 78.35% | 52.93% | 63.18% | 90.37% |
| Logistic Regression | 85.19% | 73.29% | 60.54% | 66.31% | 90.45% |

Hasil pendekatan sederhana dengan fitur sensitif dikeluarkan (`race`, `sex`, `native.country`):

| Model valid sederhana | Accuracy | Precision `>50K` | Recall `>50K` | F1 `>50K` | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Decision Tree `max_depth=5` | 84.85% | 76.59% | 53.40% | 62.93% | 88.36% |
| Decision Tree `max_depth=8`, `min_samples_leaf=50` | 85.18% | 78.46% | 52.98% | 63.25% | 90.36% |
| Logistic Regression | 85.08% | 73.31% | 59.78% | 65.85% | 90.32% |

Catatan penting: angka di atas adalah estimasi ulang sederhana untuk review teknis, bukan hasil resmi notebook lama. Untuk portfolio final, angka performa harus direproduksi di notebook baru atau script training yang bersih.

### Kesimpulan accuracy realistis

Accuracy yang masuk akal untuk versi awal portfolio kemungkinan berada di sekitar:

```text
84% sampai 86%
```

Angka ini jauh lebih realistis daripada 100%. Untuk recruiter, hasil 85% dengan pipeline valid lebih kuat daripada 100% yang bocor.

---

## 7. Preprocessing

### Preprocessing pada notebook lama

Notebook lama melakukan beberapa langkah preprocessing:

1. mengganti `?` menjadi `NaN`;
2. mengisi missing value dengan median;
3. melakukan mapping kategori manual ke angka;
4. mengubah beberapa kolom menjadi integer;
5. membuat `cluster` dari target;
6. memakai `LabelEncoder`;
7. melakukan train-test split.

Beberapa langkah tersebut perlu diperbaiki.

### Masalah preprocessing lama

#### 1. Preprocessing dilakukan sebelum train-test split

Imputasi dan encoding dilakukan sebelum data dibagi menjadi train dan test. Ini berpotensi membuat informasi dari test set masuk ke proses training.

Untuk portfolio final, urutan yang benar:

```text
split data -> fit preprocessing pada train -> transform train/test -> train model -> evaluasi test
```

#### 2. Mapping kategori manual berisiko

Notebook melakukan mapping kategori ke angka. Contoh:

```python
A2 = {'Private': 1, 'State_gov': 2, 'Federal-gov': 3, ...}
```

Namun dataset memakai nilai:

```text
State-gov
```

bukan:

```text
State_gov
```

Akibatnya, kategori `State-gov` tidak ter-map dengan benar.

#### 3. Angka manual pada kategori dapat menciptakan urutan palsu

Contoh: `Private = 1`, `Self-emp-not-inc = 5`, `Without-pay = 8` tidak berarti ada urutan matematis yang benar. Untuk model tree, ini masih bisa menimbulkan split yang kurang natural.

#### 4. `LabelEncoder` tidak ideal untuk fitur kategorikal

`LabelEncoder` lebih cocok untuk target label, bukan fitur kategorikal multi-kategori. Untuk fitur kategorikal, gunakan:

```text
OneHotEncoder
```

atau pendekatan lain yang memang dirancang untuk fitur kategorikal.

### Preprocessing yang direkomendasikan

Gunakan `ColumnTransformer` dan `Pipeline`:

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

numeric_features = [
    'age',
    'education.num',
    'capital.gain',
    'capital.loss',
    'hours.per.week'
]

categorical_features = [
    'workclass',
    'education',
    'marital.status',
    'occupation',
    'relationship'
]

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)
```

Untuk Decision Tree, `StandardScaler` tidak wajib. Namun jika ingin membandingkan dengan Logistic Regression, scaler membantu menjaga pipeline tetap konsisten.

---

## 8. Model yang lebih layak untuk demo

Model lama menggunakan Decision Tree. Decision Tree masih boleh dipakai untuk portfolio karena mudah divisualisasikan dan mudah dijelaskan. Namun, model lama harus dilatih ulang dengan fitur valid.

### Opsi model untuk demo

#### Opsi 1 — Logistic Regression

Kelebihan:

- ringan;
- cepat;
- mudah dijelaskan;
- menghasilkan probabilitas;
- performa valid sederhana sekitar 85% pada simulasi ulang.

Kekurangan:

- interpretasi koefisien bisa menjadi panjang setelah OneHotEncoding;
- kurang fleksibel dibanding model ensemble.

Cocok untuk:

```text
versi demo pertama yang stabil dan mudah dijelaskan
```

#### Opsi 2 — Decision Tree yang dibatasi

Contoh parameter:

```text
max_depth=5 sampai 8
min_samples_leaf=50
```

Kelebihan:

- mudah divisualisasikan;
- mudah dijelaskan kepada recruiter non-ML;
- cocok untuk menjelaskan decision path.

Kekurangan:

- rawan overfitting jika terlalu dalam;
- performa bisa kalah dari model ensemble;
- perlu pembatasan depth dan leaf.

Cocok untuk:

```text
portfolio yang ingin menonjolkan interpretability
```

#### Opsi 3 — Random Forest / Gradient Boosting

Kelebihan:

- biasanya lebih kuat;
- lebih stabil daripada single decision tree;
- cocok untuk demo prediksi.

Kekurangan:

- lebih sulit dijelaskan;
- lebih berat untuk deployment kecil;
- perlu penjelasan tambahan jika recruiter ingin memahami model.

Cocok untuk:

```text
versi lanjutan setelah baseline dan Decision Tree valid selesai
```

### Rekomendasi final untuk demo

Untuk project portfolio ini, rekomendasi terbaik:

```text
Logistic Regression atau Decision Tree terbatas sebagai model utama demo.
```

Jika ingin sederhana dan stabil, pilih:

```text
Logistic Regression + preprocessing pipeline
```

Jika ingin mudah divisualisasikan, pilih:

```text
DecisionTreeClassifier(max_depth=5 atau 8, min_samples_leaf=50)
```

Jangan gunakan model dari notebook lama sampai target leakage diperbaiki.

---

## 9. Input prediction form yang aman

Demo recruiter sebaiknya dibuat sebagai form sederhana, misalnya dengan Streamlit.

### Input yang direkomendasikan

Gunakan input berikut:

| Input form | Tipe | Contoh |
|---|---|---|
| Age | number input | 35 |
| Workclass | selectbox | Private, Self-emp-not-inc, Federal-gov |
| Education | selectbox | Bachelors, HS-grad, Masters |
| Education Number | number input atau otomatis dari education | 13 |
| Marital Status | selectbox | Never-married, Married-civ-spouse |
| Occupation | selectbox | Exec-managerial, Craft-repair, Sales |
| Relationship | selectbox | Husband, Not-in-family, Own-child |
| Capital Gain | number input | 0 |
| Capital Loss | number input | 0 |
| Hours per Week | number input | 40 |

### Input yang sebaiknya tidak ditampilkan

Jangan tampilkan input berikut di form demo publik:

```text
race
sex
native.country
```

Alasan:

- termasuk atribut sensitif atau berpotensi sensitif;
- dapat menimbulkan pertanyaan fairness;
- tidak diperlukan untuk membuat demo portfolio yang kuat;
- simulasi ulang menunjukkan performa tetap sekitar 85% meskipun fitur sensitif dikeluarkan.

### Input yang perlu dipertimbangkan ulang

```text
fnlwgt
```

Alasan:

- kurang intuitif untuk recruiter;
- user demo kemungkinan tidak tahu harus mengisi apa;
- lebih baik dikeluarkan dari model demo atau diisi otomatis jika benar-benar diperlukan.

### Validasi input form

Tambahkan validasi sederhana:

- `age` minimal 17 atau 18;
- `hours.per.week` antara 1 sampai 100;
- `capital.gain` minimal 0;
- `capital.loss` minimal 0;
- semua selectbox hanya berisi kategori yang pernah muncul di training data.

---

## 10. Output yang perlu dijelaskan ke recruiter

Output demo jangan hanya menampilkan label prediksi. Tampilkan juga konteks agar recruiter melihat bahwa project ini dipahami secara profesional.

### Output utama

Contoh output:

```text
Predicted income class: >50K
Prediction probability: 72.4%
```

atau:

```text
Predicted income class: <=50K
Prediction probability: 81.6%
```

### Output pendukung

Tambahkan penjelasan:

1. **Model yang digunakan**

   Contoh:

   ```text
   Model: Logistic Regression with preprocessing pipeline
   ```

2. **Dataset**

   Contoh:

   ```text
   Dataset: Adult Income dataset, 32,561 rows, binary target <=50K / >50K
   ```

3. **Baseline**

   Contoh:

   ```text
   Majority-class baseline accuracy: 75.92%
   ```

4. **Model performance**

   Contoh:

   ```text
   Test accuracy: around 85% after removing target leakage
   ```

5. **Important limitation**

   Contoh:

   ```text
   This demo is for portfolio and learning purposes only. It should not be used for real financial, employment, or eligibility decisions.
   ```

6. **Fairness note**

   Contoh:

   ```text
   Sensitive attributes such as race, sex, and native country are excluded from the public demo form to reduce fairness risks.
   ```

7. **Interpretability note**

   Jika memakai Decision Tree:

   ```text
   The decision tree is depth-limited to reduce overfitting and improve interpretability.
   ```

   Jika memakai Logistic Regression:

   ```text
   The model estimates probability based on encoded demographic and work-related features.
   ```

---

## 11. Cara menjelaskan project ini saat interview

Penjelasan yang jujur dan kuat:

```text
This project started as an academic notebook. During portfolio preparation, I audited the original model and found that the previous 100% accuracy was caused by target leakage. I then redesigned the modeling approach by removing leakage, using valid input features, applying preprocessing through a pipeline, comparing the model against a majority-class baseline, and preparing a safer demo form that excludes sensitive attributes.
```

Versi Bahasa Indonesia:

```text
Project ini awalnya berasal dari notebook kuliah. Saat saya siapkan untuk portfolio, saya melakukan audit dan menemukan bahwa accuracy 100% pada versi lama disebabkan oleh target leakage. Karena itu, saya mendesain ulang pendekatan model dengan menghapus fitur yang bocor dari target, memakai fitur input yang valid, membuat preprocessing pipeline, membandingkan hasil dengan baseline kelas mayoritas, dan menyiapkan form demo yang lebih aman tanpa atribut sensitif.
```

Poin ini justru bisa menjadi nilai tambah karena menunjukkan kemampuan:

- membaca ulang source code lama secara kritis;
- menemukan leakage;
- tidak asal percaya accuracy tinggi;
- memperbaiki pipeline ML;
- memahami fairness dan deployment demo.

---

## 12. Checklist sebelum demo dipublikasikan

Sebelum project dipublikasikan di GitHub atau website portfolio, pastikan:

- [ ] `Class` tidak masuk ke fitur model.
- [ ] `cluster` dari target tidak dipakai.
- [ ] Semua fitur target leakage dihapus.
- [ ] Data dibagi dengan `train_test_split(..., stratify=y)`.
- [ ] Preprocessing memakai `Pipeline` dan `ColumnTransformer`.
- [ ] Encoding kategori memakai `OneHotEncoder(handle_unknown='ignore')`.
- [ ] Missing value ditangani dalam pipeline.
- [ ] Model dibandingkan dengan baseline 75.92%.
- [ ] Evaluasi memakai accuracy, precision, recall, F1-score, ROC-AUC, dan confusion matrix.
- [ ] Accuracy 100% dari notebook lama tidak dipakai sebagai klaim final.
- [ ] Demo form tidak meminta `race`, `sex`, dan `native.country`.
- [ ] Output demo menampilkan prediksi, probabilitas, baseline, performa, dan limitation note.
- [ ] README menjelaskan bahwa project sudah diaudit dan model lama diperbaiki.

---

## 13. Kesimpulan review model

Model pada notebook lama belum layak dijadikan model final karena mengalami target leakage. Hasil accuracy 100% harus dihapus dari klaim performa utama.

Project ini tetap sangat bisa diselamatkan untuk portfolio. Dengan pipeline yang benar, fitur valid, evaluasi realistis, dan demo yang aman, project dapat diposisikan sebagai:

```text
Income Prediction Machine Learning App with Leakage-Aware Model Review
```

Nilai jual terbaik project ini bukan “akurasi 100%”, melainkan kemampuan untuk:

- mengaudit model lama;
- menemukan leakage;
- memperbaiki pipeline;
- membuat evaluasi realistis;
- mengubah notebook akademik menjadi demo machine learning yang siap portfolio.
