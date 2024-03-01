from flask import Flask, render_template, request
from flask import redirect, url_for, session
from pydantic import BaseModel, field_validator, ValidationError

import os, sys
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/history/")
def history():
    return render_template('history.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')

@app.route("/register/")
def register():
    return render_template('register.html')

@app.route("/trade/")
def trade():
    return render_template('trade.html')

