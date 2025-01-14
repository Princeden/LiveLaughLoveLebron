# Princeden Hom, Kyle Lee, Sascha Gordon-Zolov, Nafiyu Murtaza
# Team LiveLaughLoveLebron
# SoftDev
# p012
# 2024-1-10

#import
import sqlite3 
import csv
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from build_db import setup_database
from werkzeug.security import generate_password_hash, check_password_hash
users_in_game = []

def get_db_connection():
    conn = sqlite3.connect('db.db')
    conn.row_factory = sqlite3.Row
    return conn
#app
app = Flask(__name__)    
app.secret_key = os.urandom(32)
#home

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route("/")
def home():
    if 'username' in session:
        username = session['username']
        conn = get_db_connection()
        user_data = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return render_template('home.html', user=user_data)
    else:
        return render_template('home.html', user=None)

@app.route("/add_to_game", methods=['GET', 'POST'])
def add_to_game():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    if not user:
        flash('Username does not exist.', 'danger')
        return render_template("lobby.html", users=users_in_game)
    elif not check_password_hash(user['password_hash'], password):
        flash('Incorrect password.', 'danger')
        return render_template("lobby.html", users=users_in_game)
    elif username not in users_in_game:
        users_in_game.append(username)
        print(users_in_game)
        return render_template("lobby.html", users=users_in_game)
    else: 
        flash('User already in game', 'danger')
        return render_template("lobby.html", users=users_in_game)
    return render_template("lobby.html", users=users_in_game)


#createGame
@app.route("/lobby")
def lobby():
    if 'username' in session:
        if session['username'] not in users_in_game:
            users_in_game.append(session['username'])
        print(users_in_game)
        return render_template("lobby.html", users=users_in_game) #more vars soon
    else:
        return "ERROR"
#game
@app.route("/game")
def game():
    return render_template("game.html") #more vars soon
#settings
@app.route("/settings")
def settings():
    return render_template("settings.html") #more vars soon
#login and register

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if not user:
            flash('Username does not exist.', 'danger')
        elif not check_password_hash(user['password_hash'], password):
            flash('Incorrect password.', 'danger')
        else:
            session['username'] = username
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, email, password_hash, balance) VALUES (?, ?, ?, ?)',
                (username, email, password_hash, 1000)
            )
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError as e:
            existing_user = conn.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username, email)).fetchone()
            if existing_user:
                if existing_user['username'] == username:
                    flash('Username is already in use.', 'danger')
                elif existing_user['email'] == email:
                    flash('Email is already in use.', 'danger')
            else:
                flash('An unexpected error occurred.', 'danger')
        finally:
            conn.close()

    return render_template('register.html')
#debug
if __name__ == "__main__": 
    app.debug = True 
    setup_database()
    app.run()


