export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"
cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill
echo "" > $AIRFLOW_HOME/airflow-webserver.pid
echo "Airflow WebServer Stopped"
cat $AIRFLOW_HOME/airflow-scheduler.pid | xargs kill
echo "" > $AIRFLOW_HOME/airflow-scheduler.pid
echo "Airflow Scheduler Stopped"