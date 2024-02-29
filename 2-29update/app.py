from flask import Flask, render_template, request
from flask import redirect, url_for, session
from pydantic import BaseModel, field_validator, ValidationError

#run flask command
#flask --app app.py --debug run
#venv active
# venv\Scripts\activate

app = Flask(__name__)

app.secret_key = 'f9b8df2fa142b5ff52ccb37fbd7eeac168811a77d0c34e43c778a4ee73d18045'
app.debug = True
class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @field_validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()
    
@app.route("/")
def hello_world():
    return render_template('homepage.html')
@app.route("/deposit/")
def deposit():
    return render_template('deposit.html')
@app.route("/withdraw/")
def withdraw():
    return render_template('withdraw.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route('/add_stock/', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)

            # Save the form data to the session object
            session['stock_symbol'] = stock_data.stock_symbol          # NEW!!
            session['number_of_shares'] = stock_data.number_of_shares  # NEW!!
            session['purchase_price'] = stock_data.purchase_price      # NEW!!
            return redirect(url_for('stocks'))  # NEW!!

        except ValidationError as e:
            print(e)

    return render_template('add_stock.html')

@app.route('/createaccount/', methods=['GET', 'POST'])
def createaccount():
    return render_template('createaccount.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/stocks/")
def stocks():
    return render_template('stocks.html')

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')


@app.route("/depositwithdrawal/")
def depositwithdrawal():
    return render_template('depositwithdrawal.html')

@app.route("/transactions/")
def transactions():
    return render_template('transactions.html')


@app.route("/index/")
def index():
    return render_template('index.html')


@app.route("/trades/")
def trades():
    return render_template('trades.html')




