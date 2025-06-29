from flask import Flask, request, render_template, flash, send_file, redirect, url_for, flash, session, jsonify
import mysql.connector
import pickle
import pandas as pd
from openpyxl import Workbook
from io import BytesIO
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

model = pickle.load(open('model.pkl', 'rb'))

# Koneksi database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="naive-cancer"
)
db_cursor = db_connection.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = -1
    if request.method == 'POST':
        # Ambil semua fitur dari form
        AGE = int(request.form.get('AGE'))
        GENDER = int(request.form.get('GENDER'))
        SMOKING = int(request.form.get('SMOKING'))
        FINGER_DISCOLORATION = int(request.form.get('FINGER_DISCOLORATION'))
        MENTAL_STRESS = int(request.form.get('MENTAL_STRESS'))
        EXPOSURE_TO_POLLUTION = int(request.form.get('EXPOSURE_TO_POLLUTION'))
        LONG_TERM_ILLNESS = int(request.form.get('LONG_TERM_ILLNESS'))
        ENERGY_LEVEL = int(request.form.get('ENERGY_LEVEL'))
        IMMUNE_WEAKNESS = int(request.form.get('IMMUNE_WEAKNESS'))
        BREATHING_ISSUE = int(request.form.get('BREATHING_ISSUE'))
        ALCOHOL_CONSUMPTION = int(request.form.get('ALCOHOL_CONSUMPTION'))
        THROAT_DISCOMFORT = int(request.form.get('THROAT_DISCOMFORT'))
        OXYGEN_SATURATION = int(request.form.get('OXYGEN_SATURATION'))
        CHEST_TIGHTNESS = int(request.form.get('CHEST_TIGHTNESS'))
        FAMILY_HISTORY = int(request.form.get('FAMILY_HISTORY'))
        SMOKING_FAMILY_HISTORY = int(request.form.get('SMOKING_FAMILY_HISTORY'))
        STRESS_IMMUNE = int(request.form.get('STRESS_IMMUNE'))

        # Buat dataframe untuk prediksi
        input_features = pd.DataFrame([[AGE, GENDER, SMOKING, FINGER_DISCOLORATION,
                                        MENTAL_STRESS, EXPOSURE_TO_POLLUTION, LONG_TERM_ILLNESS,
                                        ENERGY_LEVEL, IMMUNE_WEAKNESS, BREATHING_ISSUE,
                                        ALCOHOL_CONSUMPTION, THROAT_DISCOMFORT, OXYGEN_SATURATION,
                                        CHEST_TIGHTNESS, FAMILY_HISTORY, SMOKING_FAMILY_HISTORY,
                                        STRESS_IMMUNE]],
                                      columns=['AGE', 'GENDER', 'SMOKING', 'FINGER_DISCOLORATION',
                                               'MENTAL_STRESS', 'EXPOSURE_TO_POLLUTION', 'LONG_TERM_ILLNESS',
                                               'ENERGY_LEVEL', 'IMMUNE_WEAKNESS', 'BREATHING_ISSUE',
                                               'ALCOHOL_CONSUMPTION', 'THROAT_DISCOMFORT', 'OXYGEN_SATURATION',
                                               'CHEST_TIGHTNESS', 'FAMILY_HISTORY', 'SMOKING_FAMILY_HISTORY',
                                               'STRESS_IMMUNE'])

        # Prediksi
        prediction = model.predict(input_features)
        prediction = int(prediction[0])

        # Simpan ke database
        insert_query = """
            INSERT INTO dataset (
                AGE, GENDER, SMOKING, FINGER_DISCOLORATION, MENTAL_STRESS,
                EXPOSURE_TO_POLLUTION, LONG_TERM_ILLNESS, ENERGY_LEVEL, IMMUNE_WEAKNESS,
                BREATHING_ISSUE, ALCOHOL_CONSUMPTION, THROAT_DISCOMFORT, OXYGEN_SATURATION,
                CHEST_TIGHTNESS, FAMILY_HISTORY, SMOKING_FAMILY_HISTORY, STRESS_IMMUNE, status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data_tuple = (AGE, GENDER, SMOKING, FINGER_DISCOLORATION, MENTAL_STRESS,
                      EXPOSURE_TO_POLLUTION, LONG_TERM_ILLNESS, ENERGY_LEVEL, IMMUNE_WEAKNESS,
                      BREATHING_ISSUE, ALCOHOL_CONSUMPTION, THROAT_DISCOMFORT, OXYGEN_SATURATION,
                      CHEST_TIGHTNESS, FAMILY_HISTORY, SMOKING_FAMILY_HISTORY, STRESS_IMMUNE,
                      prediction)

        db_cursor.execute(insert_query, data_tuple)
        db_connection.commit()
    return render_template('index.html', prediction=prediction)




# # admin
# @app.route('/api/register', methods=['POST'])
# def api_register():
#     data = request.get_json()

#     email = data.get('email')
#     password = data.get('password')
#     confirm_password = data.get('confirm_password')

#     # Cek apakah email atau password kosong
#     if not email or not password or not confirm_password:
#         return jsonify({'message': 'Semua kolom harus diisi.', 'status': 'warning'}), 400

#     # Cek apakah password dan konfirmasi password sama
#     if password != confirm_password:
#         return jsonify({'message': 'Password dan konfirmasi password tidak cocok.', 'status': 'warning'}), 400

#     # Cek apakah email sudah terdaftar
#     db_cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     user = db_cursor.fetchone()

#     if user:
#         return jsonify({'message': 'Email sudah terdaftar.', 'status': 'warning'}), 400

#     # Hash password dan simpan ke database
#     hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#     db_cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
#     db_connection.commit()

#     return jsonify({'message': 'Registrasi berhasil! Silakan login.', 'status': 'success'}), 201

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Pengecekan apakah sudah login
    if 'user_id' in session:
        flash('Anda sudah login.', 'info')
        return redirect(url_for('admin'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Cek apakah email atau password kosong
        if not email or not password:
            flash('Email dan password harus diisi.', 'warning')
            return redirect(url_for('login'))

        # Cek apakah user ada di database
        db_cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = db_cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('admin'))
        else:
            flash('Login gagal. Periksa email dan password Anda.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Hapus sesi user_id
    session.pop('user_id', None)
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    # Pengecekan apakah sudah login
    if 'user_id' not in session:
        flash('Anda harus login terlebih dahulu.', 'danger')
        return redirect(url_for('login'))

    # Ambil nama pengguna yang sedang login
    db_cursor.execute("SELECT email FROM users WHERE id = %s", (session['user_id'],))
    user = db_cursor.fetchone()
    if user:
        nama_pengguna = user['email']  # Sesuaikan dengan kolom yang sesuai

        # Mengambil data dari tabel predictions dan users
        select_query = """
            SELECT * FROM dataset
        """
        db_cursor.execute(select_query)
        predictions = db_cursor.fetchall()

        total_predictions = len(predictions)
        total_negatif = sum(1 for prediction in predictions if prediction['status'] == 0)
        total_positif = sum(1 for prediction in predictions if prediction['status'] == 1)

        return render_template('admin.html', nama_pengguna=nama_pengguna, predictions=predictions,total_predictions=total_predictions,
                               total_negatif=total_negatif, total_positif=total_positif)
    else:
        flash('Data pengguna tidak ditemukan.', 'danger')
        return redirect(url_for('login'))

@app.route('/report', methods=['GET'])
def report():
    # Ambil semua data dari database
    select_query = "SELECT * FROM dataset"
    db_cursor.execute(select_query)
    data = db_cursor.fetchall()

    # Buat file Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Data Prediksi"

    # Header kolom sesuai field
    ws.append([
        'Umur', 'Jenis Kelamin', 'Merokok', 'Kondisi Jari', 'Stress',
        'Paparan Polusi', 'Penyakit Jangka Panjang', 'Energi', 'Kekuatan Imun',
        'Masalah Pernafasan', 'Konsumsi Alkohol', 'Kondisi Tenggorokan', 'Saturasi Oksigen',
        'Kekakuan Dada', 'Riwayat Keluarga', 'Riwayat Keluarga Merokok', 'Stress Imun', 'Status Prediksi'
    ])

    # Loop data dan tambahkan ke Excel
    for row in data:
        ws.append([
            row['AGE'],
            'Laki-laki' if row['GENDER'] == 1 else 'Perempuan',
            'Ya' if row['SMOKING'] == 1 else 'Tidak',
            'Ya' if row['FINGER_DISCOLORATION'] == 1 else 'Tidak',
            'Ya' if row['MENTAL_STRESS'] == 1 else 'Tidak',
            'Ya' if row['EXPOSURE_TO_POLLUTION'] == 1 else 'Tidak',
            'Ya' if row['LONG_TERM_ILLNESS'] == 1 else 'Tidak',
            row['ENERGY_LEVEL'],
            row['IMMUNE_WEAKNESS'],
            'Ya' if row['BREATHING_ISSUE'] == 1 else 'Tidak',
            'Ya' if row['ALCOHOL_CONSUMPTION'] == 1 else 'Tidak',
            'Ya' if row['THROAT_DISCOMFORT'] == 1 else 'Tidak',
            row['OXYGEN_SATURATION'],
            'Ya' if row['CHEST_TIGHTNESS'] == 1 else 'Tidak',
            'Ya' if row['FAMILY_HISTORY'] == 1 else 'Tidak',
            'Ya' if row['SMOKING_FAMILY_HISTORY'] == 1 else 'Tidak',
            'Ya' if row['STRESS_IMMUNE'] == 1 else 'Tidak',
            'Positif' if row['status'] == 1 else 'Negatif'
        ])

    # Simpan ke buffer memory
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name='data_prediksi_kanker.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

if __name__ == '__main__':
    app.run(debug=True)
