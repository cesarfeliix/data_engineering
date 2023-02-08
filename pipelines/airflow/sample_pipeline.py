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
    description='Sample ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)

#Task Definition
# define the tasks

# define extract task
extract = BashOperator(
    task_id='extract',
    bash_command='echo "extract"',
    dag=dag,
)

# define transform task
transform = BashOperator(
    task_id='transform',
    bash_command='echo "transform"',
    dag=dag,
)

# define load task
load = BashOperator(
    task_id='load',
    bash_command='echo "load"',
    dag=dag,
)

#Task Pipeline
extract >> transform >> load
