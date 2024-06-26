from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def redirect_to_welcome():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    # Add logic here to handle main application page
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_schedule():
    # Add logic here to handle adding schedule
    return redirect(url_for('home'))

@app.route('/check_reminder')
def check_reminder():
    # Add logic here to handle reminder checking
    return redirect(url_for('home'))

@app.route('/test')
def test():
    return "This is a test page!"
