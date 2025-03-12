import os
import logging
import pandas as pd
from etl import run_etl
from model import run_all_models
from visualization import generate_summary_statistics, plot_crime_trends, export_clustered_data
from config import LOG_FILE, PROCESSED_DATA_DIR, DATA_FILE

def setup_logging():
    """
    Configure logging to file and console.
    """
    # Create log directory if it doesn't exist.
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )
    logging.getLogger().addHandler(logging.StreamHandler())

def main():
    setup_logging()
    logging.info("Project started.")
    
    try:
        # --- ETL Process ---
        logging.info("Starting ETL process.")
        run_etl()
        
        # --- Load Data for ML & Visualization ---
        # For demonstration, try loading processed data if saved;
        # otherwise, load a sample from the raw dataset.
        # processed_file = os.path.join(PROCESSED_DATA_DIR, 'cleaned_data.csv')
        # if os.path.exists(processed_file):
        #     df = pd.read_csv(processed_file, parse_dates=['Date', 'Updated On'])
        # else:
        #     # Adjust nrows or remove to process full dataset.
        #     df = pd.read_csv(DATA_FILE, nrows=100000, parse_dates=['Date', 'Updated On'])
        df = pd.read_csv(DATA_FILE, parse_dates=['Date', 'Updated On'])
        
        # --- Run Machine Learning Models ---
        model_results = run_all_models(df)
        
        # --- Generate Outputs for Dashboard ---
        generate_summary_statistics(df)
        plot_crime_trends(df)
        
        # Export clustered data (from the clustering model) for dashboard usage.
        if 'clustering' in model_results and 'data' in model_results['clustering']:
            export_clustered_data(model_results['clustering']['data'])
        
        logging.info("Project completed successfully.")
    except Exception as e:
        logging.error("Project failed: %s", e)
        raise

if __name__ == "__main__":
    main()
