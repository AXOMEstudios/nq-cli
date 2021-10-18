from flask import Flask, render_template, redirect, session, g, request, flash
from os import getenv

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

app.run()