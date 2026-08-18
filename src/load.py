import logging
from sqlalchemy import create_engine

# Configure logging for database operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_database_engine(user, password, host, port, database):
    """
    Creates and returns a SQLAlchemy database engine connection.
    """
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine

def load_to_database(df, table_name, engine):
    """
    Loads a cleaned Pandas DataFrame into a MySQL database table.
    """
    try:
        # Append data to existing table or create if it doesn't exist
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        logging.info(f"Successfully loaded {len(df)} records into table '{table_name}'.")
    except Exception as e:
        logging.error(f"Error loading data into database: {e}")
        raise
