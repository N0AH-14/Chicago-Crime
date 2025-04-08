import os
import pandas as pd
import matplotlib.pyplot as plt
import logging
from config import PROCESSED_DATA_DIR

def generate_summary_statistics(df):
    # Generate and save summary statistics from the dataset.
    try:
        summary = df.describe(include='all')
        output_path = os.path.join(PROCESSED_DATA_DIR, 'summary_statistics.csv')
        summary.to_csv(output_path)
        logging.info("Summary statistics saved to %s", output_path)
        return summary
    except Exception as e:
        logging.error("Error generating summary statistics: %s", e)
        raise

def plot_crime_trends(df):
    # Plot and save the trend of crimes per year.
    try:
        crime_counts = df.groupby('Year').size()
        plt.figure(figsize=(10, 6))
        crime_counts.plot(kind='line', marker='o')
        plt.title('Number of Crimes per Year')
        plt.xlabel('Year')
        plt.ylabel('Crime Count')
        plt.grid(True)
        output_path = os.path.join(PROCESSED_DATA_DIR, 'crime_trends.png')
        plt.savefig(output_path)
        plt.close()
        logging.info("Crime trends plot saved to %s", output_path)
    except Exception as e:
        logging.error("Error plotting crime trends: %s", e)
        raise

def export_clustered_data(clustered_df):
    # Export clustered data to CSV for use in dashboards.
    try:
        output_path = os.path.join(PROCESSED_DATA_DIR, 'clustered_data.csv')
        clustered_df.to_csv(output_path, index=False)
        logging.info("Clustered data exported to %s", output_path)
    except Exception as e:
        logging.error("Error exporting clustered data: %s", e)
        raise
