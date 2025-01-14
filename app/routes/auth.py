# Princeden Hom, Kyle Lee, Sascha Gordon-Zolov, Nafiyu Murtaza
# Team LiveLaughLoveLebron
# SoftDev
# p012
# 2024-1-14

import sqlite3
import csv
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from build_db import setup_database
from werkzeug.security import generate_password_hash, check_password_hash

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

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))
