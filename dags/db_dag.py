from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import main

args = {
    'owner': 'Nikita Kostin',
    'start_date': days_ago(1)  # make start date in the past
}

dag = DAG(
    dag_id='cannabis-dags',
    default_args=args,
    schedule_interval='*/10 * * * *'
)

with dag:
    second_dag = PythonOperator(
        task_id='insert_data',
        python_callable=main.main
    )

