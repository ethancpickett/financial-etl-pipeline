import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_from_csv(file_path):
    """
    Extracts raw financial data from a flat CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Extraction successful: Read {len(df)} rows from {file_path}.")
        return df
    except Exception as e:
        logging.error(f"Failed to extract data from {file_path}: {e}")
        raise
