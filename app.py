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
        Age = int(request.form.get('Age'))
        Gender = int(request.form.get('Gender'))
        Air_Pollution = int(request.form.get('Air_Pollution'))
        Obesity = int(request.form.get('Obesity'))
        Passive_Smoker = int(request.form.get('Passive_Smoker'))
        Fatigue = int(request.form.get('Fatigue'))
        Weight_Loss = int(request.form.get('Weight_Loss'))
        Wheezing = int(request.form.get('Wheezing'))
        Swallowing_Difficulty = int(request.form.get('Swallowing_Difficulty'))
        Clubbing_of_Finger_Nails = int(request.form.get('Clubbing_of_Finger_Nails'))

        # Buat dataframe untuk prediksi (harus sesuai urutan fitur yang dipakai model)
        input_features = pd.DataFrame([[Age, Gender, Air_Pollution, Obesity,
                                        Passive_Smoker, Fatigue, Weight_Loss,
                                        Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails]],
                                      columns=['Age', 'Gender', 'Air Pollution', 'Obesity',
                                               'Passive Smoker', 'Fatigue', 'Weight Loss',
                                               'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails'])

        # Prediksi
        prediction = model.predict(input_features)
        prediction = int(prediction[0])

        # Simpan ke database
        insert_query = """
            INSERT INTO dataset (
                Age, Gender, Air_Pollution, Obesity, Passive_Smoker,
                Fatigue, Weight_Loss, Wheezing, Swallowing_Difficulty,
                Clubbing_of_Finger_Nails, status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data_tuple = (Age, Gender, Air_Pollution, Obesity, Passive_Smoker,
                      Fatigue, Weight_Loss, Wheezing, Swallowing_Difficulty,
                      Clubbing_of_Finger_Nails, prediction)

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
        total_low = sum(1 for prediction in predictions if prediction['status'] == 0)
        total_medium = sum(1 for prediction in predictions if prediction['status'] == 1)
        total_high = sum(1 for prediction in predictions if prediction['status'] == 2)

        return render_template('admin.html', nama_pengguna=nama_pengguna, predictions=predictions,total_predictions=total_predictions,
                               total_low=total_low, total_medium=total_medium, total_high=total_high)
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
    # Header Excel
    ws.append([
        'Age', 'Gender', 'Air Pollution', 'Obesity', 'Passive Smoker',
        'Fatigue', 'Weight Loss', 'Wheezing', 'Swallowing Difficulty',
        'Clubbing of Finger Nails', 'Status'
    ])

    # Loop data dan tambahkan ke Excel
    for row in data:
        ws.append([
            row['Age'],
            'Male' if row['Gender'] == 1 else 'Female',
            row['Air_Pollution'],
            row['Obesity'],
            row['Passive_Smoker'],
            row['Fatigue'],
            row['Weight_Loss'],
            row['Wheezing'],
            row['Swallowing_Difficulty'],
            row['Clubbing_of_Finger_Nails'],
           'Low' if row['status'] == 0 else 'Medium' if row['status'] == 1 else 'High'
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
