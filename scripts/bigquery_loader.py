"""
bigquery_loader.py
Handles loading pandas DataFrame into Google BigQuery.
"""

from google.cloud import bigquery
import pandas_gbq

def load_to_bigquery(df, bq_config):
    """
    Appends data to BigQuery table.
    :param df: pandas DataFrame
    :param bq_config: dict with project_id, dataset, table
    """
    project_id = bq_config["project_id"]
    dataset = bq_config["dataset"]
    table = bq_config["table"]

    table_id = f"{project_id}.{dataset}.{table}"

    print(f"Loading {len(df)} records into {table_id}...")

    pandas_gbq.to_gbq(
        df,
        table_id,
        project_id=project_id,
        if_exists="append"
    )

    print("✅ Load complete!")
