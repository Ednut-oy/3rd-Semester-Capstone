from airflow import DAG
import os
from datetime import datetime, timedelta
from web.operators.AirTraffic_Operator import WebToGCSHKOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator

# Define your default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 11, 20),
    "email": [os.getenv("ALERT_EMAIL", "")],
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "email_on_failure": True,  # Send email on task failure
    "email_on_retry": False,  # Do not send email on task retries
}

# Retrieve environment variables
PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = "bascket1" #os.environ.get("GCP_GCS_BUCKET")
DATASET = "3rd_semester_project"
OBJECT = "Air_Traffic_Data"

# Database configuration
PG_HOST = os.environ.get("PG_HOST")
PG_PORT = os.environ.get("PG_PORT")
PG_DATABASE = os.environ.get("PG_DATABASE")
PG_USER = os.environ.get("PG_USER")
PG_PASSWORD = os.environ.get("PG_PASSWORD")

# Create your DAG with a unique identifier ('data_fetch_dag')
with DAG(
    dag_id="Load-AirTraffic-Data-From-Web-To-GCS-To-BQ",
    default_args=default_args,
    description="Job to move from API-To-GCS-To-BQ",
    schedule_interval="@daily",
    max_active_runs=1,
    catchup=True,
    tags=["Data_To_BQ"]
) as dag:
    # Create a starting dummy operator
    start = DummyOperator(task_id='start')

    # Fetch and store data from an API into Google Cloud Storage
    download_to_gcs = WebToGCSHKOperator(
        task_id='download_from_API_to_Postgres', # Specify the GCS object name
        api_endpoint='https://data.sfgov.org/resource/rkru-6vcg.json',  # API endpoint URL
        api_headers={
            "X-App-Token": 'iVZ2PmRbEMzeDsMed3YOEGR14',  # API token header
            "X-App-Secret": '6DIspwu9IFPtodKTbu0Q-WRjSz1URd47bXnO',  # API secret header
        },
        api_params={
            "$limit": 34000,  # API parameters
        },
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT,
        db=PG_DATABASE,
    )

    get_data = PostgresToGCSOperator(
        task_id="transfer_AirTraffic_data_from_Postgres_to_GCS",
        postgres_conn_id='postgres_default',
        sql=f"SELECT * FROM air_traffic_data",
        bucket=BUCKET,
        filename=f"air_traffic_data.json",
        gzip=False,
    )

    # Push data from Google Cloud Storage to BigQuery
    upload_to_bigquery = GCSToBigQueryOperator(
        task_id='upload_AirTraffic_data_to_bigquery',
        source_objects=['air_traffic_data.json'],  # Source object(s) in GCS
        destination_project_dataset_table=f"{DATASET}.{OBJECT}_table",  # Destination BigQuery table
        # schema_fields=[],  # Define schema fields if needed
        # skip_leading_rows=1,  # Skip leading rows in CSV
        source_format="NEWLINE_DELIMITED_JSON",  # Source file format
        # field_delimiter=',',  # Delimiter used in CSV
        create_disposition='CREATE_IF_NEEDED',  # Create the table if it doesn't exist
        write_disposition='WRITE_TRUNCATE',  # Overwrite existing data in the table
        autodetect=True,  # Automatically detect schema
        bucket="bascket1",  # Specify the GCS bucket
    )

    # Create a ending dummy operator
    end = DummyOperator(task_id='end')

    # Define task dependencies
    start >> download_to_gcs >> get_data >> upload_to_bigquery >> end
