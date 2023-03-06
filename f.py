from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index ():
    headline = "Hello, Hammad"
    return render_template("AB.html", headline = headline)