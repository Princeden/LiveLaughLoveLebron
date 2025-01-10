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
#app
app = Flask(__name__)    
app.secret_key = os.urandom(32)
#home
@app.route("/")
def home():
    return render_template("home.html") #more vars here soon
#createGame
@app.route("/creategame")
def createGame():
    return render_template("createGame.html") #more vars soon
#game
@app.route("/game")
def game():
    return render_template("game.html") #more vars soon
#settings
@app.route("/settings")
def settings():
    return render_template("settings.html") #more vars soon
#login and register
@app.route("/login")
def login():
    return render_template("login.html") #more vars soon, setup both login and register here
#debug
if __name__ == "__main__": 
    app.debug = True 
    app.run()


