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

#setup db
#db setup goes here

#main import
from app.routes import *

#debug
if __name__ == "__main__":
    app.debug = True
    setup_database()
    app.run()
