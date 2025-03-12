import os
import pandas as pd
import logging
from config import DATA_FILE, PROCESSED_DATA_DIR
from transform import clean_data
from database import get_engine, create_tables

def extract_data():
    """
    Extract data from the CSV file in chunks.
    """
    try:
        logging.info("Data extraction started.")
        # Using chunksize for large datasets.
        chunks = pd.read_csv(DATA_FILE, chunksize=1000000, parse_dates=['Date', 'Updated On'])
        for chunk in chunks:
            yield chunk
    except Exception as e:
        logging.error("Error extracting data: %s", e)
        raise

def load_data_to_db(df):
    """
    Load the transformed DataFrame into the MySQL database.
    """
    try:
        engine = get_engine()
        create_tables(engine)
        # Write the DataFrame to the 'crimes' table.
        df.to_sql(name='crimes', con=engine, if_exists='append', index=False, method='multi')
        logging.info("Loaded %d records to the database.", len(df))
    except Exception as e:
        logging.error("Error loading data to the database: %s", e)
        raise

def run_etl():
    """
    Run the full ETL pipeline.
    """
    try:
        n=0
        for chunk in extract_data():
            # Clean and transform the data.
            # if n==1:
            #     break
            # n+=1
            cleaned_chunk = clean_data(chunk)
            # cleaned_chunk.to_csv(os.path.join(PROCESSED_DATA_DIR, 'cleaned_data.csv'), mode='a', index=False)
            load_data_to_db(cleaned_chunk)
        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error("ETL process failed: %s", e)
        raise
