"""
etl_pipeline.py
Main entrypoint for Weather ETL pipeline.
Loops through cities, fetches weather data, saves raw JSON,
and loads cleaned data into BigQuery.
"""

import os
import json
from datetime import datetime
import requests
import yaml
import pandas as pd

from bigquery_loader import load_to_bigquery
from utils import clean_weather_data, get_city_list

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["api_key"]
CITIES = config["cities"]
RAW_DATA_DIR = "raw_data/"

os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_weather(city: str):
    """Fetch weather data from OpenWeatherMap API (example)."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    all_data = []
    
    for city in get_city_list(CITIES):
        print(f"Fetching weather for {city}...")
        data = fetch_weather(city)

        # Save raw JSON backup
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        raw_path = os.path.join(RAW_DATA_DIR, f"{city}_{timestamp}.json")
        with open(raw_path, "w") as f:
            json.dump(data, f, indent=2)

        # Transform into DataFrame row
        df = clean_weather_data(data)
        all_data.append(df)

    # Combine all cities into one DataFrame
    final_df = pd.concat(all_data, ignore_index=True)

    # Load into BigQuery
    load_to_bigquery(final_df, config["bigquery"])

if __name__ == "__main__":
    main()
