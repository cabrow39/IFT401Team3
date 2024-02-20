from flask import Flask, render_template
import datetime

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello_world():
    return render_template('homepage.html')


@app.route("/contact/")
def contact():
    return render_template('contact.html',
    utc_dt=datetime.datetime.utcnow())

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')


@app.route("/depositwithdrawal/")
def depositwithdrawal():
    return render_template('depositwithdrawal.html')

@app.route("/transactions/")
def transactions():
    return render_template('transactions.html')


@app.route("/stocks/")
def stocks():
    return render_template('stocks.html')

