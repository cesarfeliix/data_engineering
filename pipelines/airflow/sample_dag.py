# The code below lists a series of airflow instructions to generate a dag (an automated and scheduled data pipeline using apache airflow and bash scripting)
# Author: Cesar R. Felix
# Date: Feb 7, 2023 at 11:30 PM

# IMPORTS
from datetime import timedelta
from airflow import DAG
from airflow.operator.bash_operator import bash_operator
from airflow.utils.dates import days_ago

#DAG Arguments
default_args = {
    'owner': 'Cesar Felix',
    'start_date': days_ago(0),
    'email': ['feliixcesar@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#DAG Definition
dag = DAG(
    dag_id='sample-etl-dag',
    default_args=default_args,
    description='Simple ETL DAG',
    schedule_interval=timedelta(days=1),
)

#Task Definition
# define the tasks

# define extract task
extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)

# define transform  and load task
transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/transformed-data.csv',
    dag=dag,
)

#Task Pipeline
extract >> transform_and_load
