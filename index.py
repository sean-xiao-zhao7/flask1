from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index(name=None):
    return render_template('index.html', person=name)
