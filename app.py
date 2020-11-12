from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/cheese")
def some_cheese():
    return "<h1> I love the stuff </h1>"

@app.route("/report")
def some_report():
    return render_template("index.html")
