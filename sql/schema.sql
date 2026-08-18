-- Create the financial data warehouse database
CREATE DATABASE IF NOT EXISTS financial_dw;
USE financial_dw;

-- Create the cleaned transactions staging/production table
CREATE TABLE IF NOT EXISTS cleansed_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id VARCHAR(50) NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    category VARCHAR(100),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
