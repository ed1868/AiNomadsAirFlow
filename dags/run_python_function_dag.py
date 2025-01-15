from datetime import datetime, timedelta

# For Airflow 2.0+:
from airflow import DAG
from airflow.operators.python import PythonOperator

def my_python_function():
    print("Hello from my Python function!")
    # Your script logic goes here
    # e.g. read/write from DB, call APIs, etc.

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='run_python_function',
    default_args=default_args,
    description='DAG that runs a Python function every minute',
    # Cron expression for "every minute":
    schedule_interval='* * * * *',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    run_script_task = PythonOperator(
        task_id='run_my_python_function',
        python_callable=my_python_function
    )

    run_script_task
