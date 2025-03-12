import pandas as pd
import logging

def clean_data(df):
    """
    Perform data cleaning and transformation on the DataFrame.
    """
    try:
        logging.info("Data cleaning started.")
        # Fill missing values in text columns.
        text_columns = ['Case Number', 'Block', 'IUCR', 'Primary Type', 
                        'Description', 'Location Description', 'Beat', 
                        'District', 'Community Area', 'FBI Code']
        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].fillna('')
        
        # Fill missing boolean fields with False.
        boolean_columns = ['Arrest', 'Domestic']
        for col in boolean_columns:
            if col in df.columns:
                df[col] = df[col].fillna(False)
        
        # Convert the Year column to integer.
        if 'Year' in df.columns:
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
        
        # Convert numeric columns.
        numeric_columns = ['X Coordinate', 'Y Coordinate', 'Latitude', 'Longitude']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Ensure datetime columns are parsed correctly.
        datetime_columns = ['Date', 'Updated On']
        for col in datetime_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # (Optional) Create a 'location' column for geospatial operations.
        # In MySQL, you might need to handle POINT types differently.

        if 'Location' in df.columns:
            df = df.drop(columns=['Location'])

        logging.info("Data cleaning completed successfully.")
        return df
    except Exception as e:
        logging.error("Error cleaning data: %s", e)
        raise