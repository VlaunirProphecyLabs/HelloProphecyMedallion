from ew9lz_eqkbzridtkugqjfg_.utils import *

@task_wrapper(task_id = "raw_bronze")
def raw_bronze(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "raw_bronze",
        json = {"task_key" : "raw_bronze"},
        databricks_conn_id = "",
    )
