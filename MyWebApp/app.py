import requests
import os
from flask import Flask, render_template, request, redirect, flash
import psycopg2


app = Flask(__name__)


conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="123",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if records:
        return render_template('account.html', full_name = records[0][1])
    else:
        flash('Неверный логин или пароль')
        return redirect('/login/')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        cursor.execute("SELECT * FROM service.users WHERE login=%s", (str(login),))
        records = list(cursor.fetchall())
        if records:
            flash ('Такой пользователь уже есть')
        else:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',(str(name), str(login), str(password)))
            conn.commit()
            return redirect('/login/')
    return render_template('registration.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run()
