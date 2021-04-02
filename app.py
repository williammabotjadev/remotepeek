from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"] )
def login():
    return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"] )
def login():
    return render_template("signup.html")

@app.route('/demo', methods=["GET", "POST"] )
def login():
    return render_template("demo.html")