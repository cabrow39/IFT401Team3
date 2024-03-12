from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    def __init__(self, first_name, last_name, email, username, balance, password, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.balance = balance
        self.password = password
        self.admin = admin

    def __repr__(self):
        return f'<User {self.username}>'

class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    quantity = db.Column(db.Float, nullable=False)
    

    user = db.relationship("User", back_populates="portfolios")
    stock = db.relationship("Stock", back_populates="portfolios")

    def __init__(self, user_id, stock_id, quantity):
        self.user_id = user_id
        self.stock_id = stock_id
        self.quantity = quantity

    def __repr__(self):
        return f'<Portfolio User:{self.user_id} Stock:{self.stock_id}>'

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    transaction_type = db.Column(db.Enum('BUY', 'SELL', name='transaction_types'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price_per_share = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("User", back_populates="transactions")
    stock = db.relationship("Stock", back_populates="transactions")

    def __init__(self, user_id, stock_id, transaction_type, quantity, price_per_share, total_cost):
        self.user_id = user_id
        self.stock_id = stock_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.price_per_share = price_per_share
        self.total_cost = total_cost

    def __repr__(self):
        return f'<Transaction User:{self.user_id} Stock:{self.stock_id} Type:{self.transaction_type}>'

class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, default=db.func.now())

    portfolios = db.relationship("Portfolio", back_populates="stock")
    transactions = db.relationship("Transaction", back_populates="stock")

    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    def __repr__(self):
        return f'{self.ticker} at {self.price}'
