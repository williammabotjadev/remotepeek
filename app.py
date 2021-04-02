from flask import Flask, render_template
from flask_wtf import request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"] )
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"] )
def signup():
    return render_template("signup.html")

@app.route('/demo', methods=["GET", "POST"] )
def demo():
    return render_template("demo.html")