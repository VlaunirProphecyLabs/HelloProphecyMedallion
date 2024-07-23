from ew9lz_eqkbzridtkugqjfg_.utils import *

@task_wrapper(task_id = "silver_customers")
def silver_customers(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "silver_customers",
        json = {"task_key" : "silver_customers"},
        databricks_conn_id = "",
    )
