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

#settings
@app.route("/settings")
def settings():
    return render_template("settings.html") #more vars soon
