from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', name='Index')


@app.route("/login")
def login():
    return render_template('index.html', name='Login')


@app.route("/home")
def home():
    return render_template('index.html', name='home')


@app.route("/profile/<username>")
def profile(username):
    return render_template('index.html', name=username)
