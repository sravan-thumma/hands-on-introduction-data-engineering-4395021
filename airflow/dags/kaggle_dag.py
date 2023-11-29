import pandas as pd
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.task_group import TaskGroup
import os

data_path = '/workspaces/hands-on-introduction-data-engineering-4395021/airflow/dataset_temp'

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}



def csvToDB():
    print("Load");


with DAG(
        dag_id='airflow_stores_pg_etl',
        schedule_interval='@daily',
        start_date=datetime(year=2023, month=11, day=28),
        catchup=False
) as dag:
    task_download_dataset = BashOperator(task_id='download_dataset',
                                 bash_command=f'kaggle datasets download kzmontage/sales-from-different-stores -p {data_path}')

    task_check_datasetzip_exists = FileSensor(task_id='check_datasetzip_exists',
                                        filepath=data_path+'/sales-from-different-stores.zip',
                                        fs_conn_id='fs_default')

    task_extract_zip = BashOperator(task_id='extract_zip',
                                    bash_command=f'unzip -o {data_path}/sales-from-different-stores.zip -d {data_path}')

    task_check_csv_file_exists = FileSensor(task_id='check_csv_file_exists',
                                            filepath=data_path+'/Different_stores_dataset.csv',
                                            fs_conn_id='fs_default')

    with TaskGroup("load", dag=dag) as load:
                csvToDB();

    task_download_dataset >> task_check_datasetzip_exists >> task_extract_zip >> task_check_csv_file_exists >> load
