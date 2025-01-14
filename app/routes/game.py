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

#add to game
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
