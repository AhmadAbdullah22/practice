from flask import Flask, render_py

app = Flask(__name__)

@app.route("/")
def index ():
    return render_py("T.html")