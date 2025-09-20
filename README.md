# 🌦️ ETL Weather API Project

This is a custom ETL pipeline I built to fetch **daily weather data** from an API, transform it, and load it into **Google BigQuery**. The data is also saved locally in `raw_data/` for backup. Finally, the dataset is connected to **Looker Studio** for visualization.

## How It Works
1. **Extract** → Pulls weather data for multiple cities.
2. **Transform** → Cleans timestamps, normalizes schema, handles duplicates.
3. **Load** → Appends daily data into BigQuery (dataset: `weather_data`).
4. **Visualize** → Connected BigQuery dataset to Looker Studio for dashboards.

## Folder Structure
- `raw_data/` → JSON backups from API
- `scripts/etl_pipeline.py` → Main entrypoint (loops through cities, runs ETL)
- `scripts/bigquery_loader.py` → Handles schema + upload to BigQuery
- `config/config.yaml` → API keys & BigQuery credentials (not in repo)
- `notebooks/` → Testing & Looker Studio prep

## Run the Pipeline
```bash
python scripts/etl_pipeline.py
```
## Requirements

Python 3.10+

Libraries: pandas, requests, google-cloud-bigquery, pandas-gbq, pyyaml

Install with:

pip install -r requirements.txt

## Config Setup

Create config
```
api_key: YOUR_API_KEY
cities: ["New York", "London", "Lagos", "Tokyo"]
bigquery:
  project_id: your-project-id
  dataset: weather_data
  table: weather_data
```
## Visualization
Connected BigQuery table → Looker Studio
Built charts by city, timestamp, and weather metrics.
Connected BigQuery table → Looker Studio

Built charts by city, timestamp, and weather metrics.
