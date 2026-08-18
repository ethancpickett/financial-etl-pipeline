import os
from src.extract import extract_from_csv
from src.transform import clean_financial_data
from src.load import get_database_engine, load_to_database

def run_pipeline():
    # Configuration paths and database credentials
    raw_file_path = "data/raw/sample_transactions.csv"

    # Database connection parameters (update with your local credentials)
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_NAME = "financial_dw"

    print("--- Starting Financial ETL Pipeline ---")

    # Step 1: Extract
    raw_df = extract_from_csv(raw_file_path)

    # Step 2: Transform
    cleaned_df = clean_financial_data(raw_file_path)

    # Step 3: Load
    engine = get_database_engine(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    load_to_database(cleaned_df, "cleansed_transactions", engine)

    print("--- ETL Pipeline Completed Successfully ---")

if __name__ == "__main__":
    run_pipeline()
