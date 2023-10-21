# views.py
from flask import render_template

def home():
    return render_template('home.html')

def profile():
    return render_template('profile.html')