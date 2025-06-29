# 🚀 Aplikasi Prediksi Risiko Kanker Paru-Paru (Naive Bayes)

Aplikasi web ini menggunakan model Naive Bayes untuk memprediksi risiko kanker paru-paru berdasarkan input pengguna. Dibangun menggunakan **Flask** dan **MySQL**.

---

## ✅ Langkah Instalasi & Menjalankan Aplikasi

### 1. Install Python & Pip (jika belum ada)

- Unduh Python dari: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Pastikan Python dan Pip sudah terinstal:

```bash
python --version
pip --version
```

---

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

---

### 3. Buat Database dan Import SQL

- Buka **phpMyAdmin** atau gunakan MySQL client
- Buat database baru dengan nama:

```sql
CREATE DATABASE `naive-cancer`;
```

- Import file `naive-cancer.sql` ke dalam database tersebut

---

### 4. Atur Koneksi Database di Python

Pastikan di file Python (misalnya `app.py`) bagian koneksi database seperti ini:

```python
# Koneksi database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="naive-cancer"
)
```

---

### 5. Jalankan Aplikasi

```bash
flask run
```

Akses aplikasi di browser: [http://localhost:5000](http://localhost:5000)

---

## ✅ Catatan Tambahan

- Pastikan MySQL/MariaDB service aktif
- Jika error `ModuleNotFoundError`, pastikan `requirements.txt` lengkap dan semua berhasil di-install
- Gunakan virtualenv jika perlu (`python -m venv venv`)

---

Selamat mencoba! 🚀
