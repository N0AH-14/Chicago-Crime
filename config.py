import os

# Path to your raw dataset file.
DATA_FILE = 'data/chicago_crime.csv'

# Directories for raw and processed data.
RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'

# Log file location.
LOG_FILE = 'logs/project.log'

# Database configuration for MySQL.
# Make sure to replace 'username' and 'password' with your actual credentials.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'ChicagoCrimeClient',         # <-- Replace with your MySQL username
    'password': 'ChicagoCrime',     # <-- Replace with your MySQL password
    'database': 'chicagocrime',
    'port': 3306
}
