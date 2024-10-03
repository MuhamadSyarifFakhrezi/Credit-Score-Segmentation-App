# Credit Scoring Analysis

## Business Understanding

Walaupun menyediakan berbagai solusi keuangan berbasis teknologi, terdapat beberapa tahapan dalam layanan yang dilakukan secara manual, salah satu tahapan tersebut ialah pemeriksaan risiko kredit ketika individu dan pelaku usaha mengajukan pinjaman. Setelah beroperasi selama satu tahun, Finance Merdeka telah mengumpulkan data yang berkaitan dengan keadaan keuangan dan kredit dari seluruh nasabah, data ini diharapkan dapat dimanfaatkan guna mengoptimalkan proses pemeriksaan risiko kredit ketika pengajuan pinjaman berlangsung.

### Permasalahan Bisnis

Tahapan pemeriksaan risiko kredit sepenuhnya dilakukan secara manual oleh tim Risk Analytics Analyst, tahapan ini tentunya memakan banyak waktu dan sangat tidak efisien, dengan mengoptimalkan tahapan ini diharapkan dapat memangkas penggunaan sumber daya perusahaan.

### Cakupan Proyek

Untuk menjawab permasalahan bisnis tersebut, kita akan menggunakan data yang telah dikumpulkan tersebut untuk mengembangkan sebuah sistem berbasis machine learning untuk memprediksi risiko kredit dari seorang pelanggan. Pada proses pengembangannya, kita akan bereksperimen dengan berbagai pendekatan atau algoritma machine learning serta membandingkannya untuk memperoleh model dengan performa terbaik, kemudian kita juga kembangkan sebuah prototipe sederhana dari sistem tersebut.

### Persiapan

Sumber data: [data.csv](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)

Setup environment:
- Via Google Colabolatory:
   1. Buka file notebook.ipynb pada Google Colaboratory
   2. Jalankan kode berikut
      ```
      !pip install -r requirements.txt
      ```
- Via Local:
   Jalankan kode berikut pada terminal/shell
   ```
   mkdir credit_scoring_customers
   cd credit_scoring_customers
   pipenv install
   pipenv shell
   pip install -r requirements.txt
   ```

### Run Streamlit App

```
streamlit run app.py
```
Link Streamlit App Prediction: [Streamlit Web App](https://student-dropout-analysis-msyarif.streamlit.app/)

## Insight

Beberapa insight yang didapat dari hasil Exploratory Data Analysis:
- Pelanggan dengan credit score baik (Good) memiliki kemampuan dalam mengelola kredit secara baik.
- Pelanggan dengan credit score yang buruk (Poor) dan standar cenderung hanya melakukan pembayaran dengan jumlah minimum seperti yang terlihat pada kolom Payment_of_Min_Amount.
- Pelanggan dengan credit score yang buruk (Poor) dan standar, biasanya memiliki profil “Low_spent_Small_value_payments” pada feature Payment_Behaviour.
- Pelanggan yang memiliki credit score baik (Good) cenderung memiliki usia yang lebih tua.
- Semakin tinggi usia riwayat kredit seorang pelanggan, semakin baik pula credit score yang dimiliki oleh pelanggan tersebut.
- Pelanggan dengan credit score yang buruk (Poor) cenderung memiliki banyak akun bank, banyak kartu kredit, jumlah utang yang banyak, serta jumlah bunga kartu kredit yang tinggi. Selain itu, mereka juga cenderung untuk melakukan penunggakan pembayaran.

### Jupyter Notebook
Link Source Code (Jupyter Notebook): [notebook.ipnyb](https://github.com/MuhamadSyarifFakhrezi/Credit-Scoring/blob/main/notebook.ipynb)
