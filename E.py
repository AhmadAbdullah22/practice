from flask import Flask, render_template 

app = Flask (__name__)


@app.route("/")
def C():
    headline = "Hello World"
    return render_template ("C.html", headline=headline)
