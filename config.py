import os

DATA_FILE = 'data/chicago_crime.csv'
RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'
LOG_FILE = 'logs/project.log'

# Database configuration for MySQL.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'ChicagoCrimeClient',
    'password': 'ChicagoCrime',
    'database': 'chicagocrime',
    'port': 3306
}
