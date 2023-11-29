#!/bin/bash
export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"
echo "Airflow WebServer Started"
echo "Airflow Scheduler Started"
airflow webserver -D
airflow scheduler
