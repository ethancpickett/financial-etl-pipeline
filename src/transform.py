import pandas as pd
import logging

# Configure logging for data quality audits
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_financial_data(file_path):
    """
    Ingests raw financial CSV data, normalizes formats, 
    removes anomalies, and validates data integrity.
    """
    try:
        # Extract
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded {file_path} with {len(df)} records.")

        # Transform & Normalize
        # Strip whitespace from string columns
        string_columns = df.select_dtypes(include=['object']).columns
        df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())

        # Standardize date format
        if 'transaction_date' in df.columns:
            df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

        # Handle missing or null financial figures
        if 'amount' in df.columns:
            initial_count = len(df)
            df = df.dropna(subset=['amount'])
            dropped_count = initial_count - len(df)
            if dropped_count > 0:
                logging.warning(f"Dropped {dropped_count} records due to missing transaction amounts.")

        # Remove duplicate entries to ensure ledger integrity
        df = df.drop_duplicates()

        logging.info("Data cleaning and normalization completed successfully.")
        return df

    except Exception as e:
        logging.error(f"Error processing financial data: {e}")
        raise
