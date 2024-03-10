from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "refresh": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("forex_data_pipeline", start_date=datetime(2024,3,1),
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available", # unique task id
        http_conn_id="forex_api", # id of the connection you are gonna to create
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b", # anything you have after the host
        response_check= lambda response: "rates" in response.text , # python function
        poke_interval=5, # check availiability every 5 seconds
        timeout=20 # seconds
    )

    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available", # unique task id
        fs_conn_id="forex_path", # id of the connection you are gonna to create
        filepath ="forex_currencies.csv",
        poke_interval=5, # check availiability every 5 seconds
        timeout=20 # seconds
    )


# Go to Airflow -> Admin -> Connections -> Add a new record
 # Restart airflow
 # Test your task with a date in the past
 #    airflow tasks test forex_data_pipeline is_forex_rates_available 2021-01-01
 #    airflow tasks test forex_data_pipeline is_forex_currencies_file_available 2021-01-01

