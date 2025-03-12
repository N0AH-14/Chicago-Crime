import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error

def run_classification(df):
    """
    Classification: Predict whether an arrest was made based on select features.
    """
    try:
        logging.info("Starting classification model training.")
        features = ['Year', 'X Coordinate', 'Y Coordinate', 'Latitude', 'Longitude']
        df = df.dropna(subset=features + ['Arrest'])
        
        X = df[features]
        y = df['Arrest'].astype(int)  # Convert boolean to int
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        logging.info("Classification model accuracy: %.2f%%", acc * 100)
        return clf, acc
    except Exception as e:
        logging.error("Error in classification model: %s", e)
        raise

def run_clustering(df, n_clusters=5):
    """
    Clustering: Group incidents based on location.
    """
    try:
        logging.info("Starting clustering model training.")
        if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
            raise ValueError("Required columns for clustering not found.")
        
        df_cluster = df.dropna(subset=['Latitude', 'Longitude'])
        X = df_cluster[['Latitude', 'Longitude']]
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df_cluster['cluster'] = kmeans.fit_predict(X)
        logging.info("Clustering completed with %d clusters.", n_clusters)
        return kmeans, df_cluster
    except Exception as e:
        logging.error("Error in clustering model: %s", e)
        raise

def run_regression(df):
    """
    Regression: Forecast the number of crimes per Year.
    """
    try:
        logging.info("Starting regression model training.")
        # Group data by Year.
        crime_counts = df.groupby('Year').size().reset_index(name='count')
        crime_counts = crime_counts[crime_counts['Year'] != 0]  # Filter out invalid Years
        
        if crime_counts.empty:
            raise ValueError("Not enough data for regression.")
        
        X = crime_counts[['Year']]
        y = crime_counts['count']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        reg = RandomForestRegressor(n_estimators=100, random_state=42)
        reg.fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        logging.info("Regression model MSE: %.2f", mse)
        return reg, mse, crime_counts
    except Exception as e:
        logging.error("Error in regression model: %s", e)
        raise

def run_all_models(df):
    """
    Run classification, clustering, and regression models.
    """
    try:
        clf, acc = run_classification(df)
        kmeans, clustered_df = run_clustering(df)
        reg, mse, crime_counts = run_regression(df)
        logging.info("All models ran successfully.")
        return {
            'classification': {'model': clf, 'accuracy': acc},
            'clustering': {'model': kmeans, 'data': clustered_df},
            'regression': {'model': reg, 'mse': mse, 'data': crime_counts}
        }
    except Exception as e:
        logging.error("Error running models: %s", e)
        raise
