from .. import app
from flask import render_template, request, redirect, url_for


users = {}


@app.route('/')
def index():
    return f'{render_template("index.html")}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
        else:
            return "Неправильне ім'я користувача або пароль"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")