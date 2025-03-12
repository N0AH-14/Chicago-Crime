from sqlalchemy import create_engine, text
from config import DB_CONFIG
import logging

def get_engine():
    """
    Create and return a SQLAlchemy engine for MySQL.
    """
    try:
        # Connection string format for MySQL via pymysql.
        conn_str = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
                   f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = create_engine(conn_str, echo=False)
        logging.info("Database engine created successfully.")
        return engine
    except Exception as e:
        logging.error("Error creating database engine: %s", e)
        raise

def create_tables(engine):
    """
    Create the crimes table if it doesn't already exist.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS crimes (
    `ID` BIGINT PRIMARY KEY,
    `Case Number` VARCHAR(255),
    `Date` DATETIME,
    `Block` VARCHAR(255),
    `IUCR` VARCHAR(50),
    `Primary Type` VARCHAR(100),
    `Description` VARCHAR(255),
    `Location Description` VARCHAR(255),
    `Arrest` BOOLEAN,
    `Domestic` BOOLEAN,
    `Beat` VARCHAR(50),
    `District` VARCHAR(50),
    `Ward` INT,
    `Community Area` VARCHAR(50),
    `FBI Code` VARCHAR(50),
    `X Coordinate` DOUBLE,
    `Y Coordinate` DOUBLE,
    `Year` INT,
    `Updated On` DATETIME,
    `Latitude` DOUBLE,
    `Longitude` DOUBLE
    );
    """
    try:
        with engine.connect() as connection:
            connection.execute(text(create_table_query))
            logging.info("Database table 'crimes' created or already exists.")
    except Exception as e:
        logging.error("Error creating database table: %s", e)
        raise
