from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    firstName = StringField(label="First Name", validators=[DataRequired()])
    lastName = StringField(label="Last Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    registerButton = SubmitField(label="Register")


app = Flask(__name__)

app.config['SECRET_KEY'] = 'u8sAAN1FngnOJzKp-fME8NpDUfFOm65r3XmYKWjw3Vs'

@app.route('/', methods=["GET", "POST"])

def index():
    form = RegisterForm()
    return render_template("index.html", form=form)

@app.route('/login', methods=["GET", "POST"] )
def login():
    return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"] )
def signup():
    return render_template("signup.html")

@app.route('/demo', methods=["GET", "POST"] )
def demo():
    return render_template("demo.html")