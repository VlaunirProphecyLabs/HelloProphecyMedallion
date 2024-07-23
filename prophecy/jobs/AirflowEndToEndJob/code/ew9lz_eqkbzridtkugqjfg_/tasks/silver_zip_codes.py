from ew9lz_eqkbzridtkugqjfg_.utils import *

@task_wrapper(task_id = "silver_zip_codes")
def silver_zip_codes(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "silver_zip_codes",
        json = {"task_key" : "silver_zip_codes"},
        databricks_conn_id = "",
    )
