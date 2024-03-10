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

def process_forex_rates():
    # This function can be used to process the forex rates once they are available
    # You can add your processing logic here
    pass

def process_forex_currencies_file():
    # This function can be used to process the forex currencies file once it is available
    # You can add your processing logic here
    pass

with DAG("forex_data_pipeline", start_date=datetime(2024, 3, 1),
         schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        http_conn_id="forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20
    )



    # Define task dependencies
    is_forex_rates_available >> is_forex_currencies_file_available

