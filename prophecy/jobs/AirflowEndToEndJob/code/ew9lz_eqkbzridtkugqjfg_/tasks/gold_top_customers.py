from ew9lz_eqkbzridtkugqjfg_.utils import *

@task_wrapper(task_id = "gold_top_customers")
def gold_top_customers(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "gold_top_customers",
        json = {"task_key" : "gold_top_customers"},
        databricks_conn_id = "",
    )
