CREATE DATABASE IF NOT EXISTS mm_database;

USE mm_database;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    password VARCHAR(100) NOT NULL,
    admin BOOLEAN DEFAULT FALSE,
);

CREATE TABLE IF NOT EXISTS stocks (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    total_shares INT,
    current_price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    stock_id INT,
    transaction_type ENUM('BUY', 'SELL') NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    price_per_share DECIMAL(10,2) NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);


CREATE TABLE IF NOT EXISTS portfolio (
    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    stock_id INT,
    quantity DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);


