import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from n9lssnycmw8k_nzphr7m0q_.tasks import DatabricksPipeline_1, SFTPToS3_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "N9LSSNycMW8k_nZphR7M0Q_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "diwYZJHb"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 5, 30, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    SFTPToS3_0_op = SFTPToS3_0()
    DatabricksPipeline_1_op = DatabricksPipeline_1()
    SFTPToS3_0_op >> DatabricksPipeline_1_op
