from n9lssnycmw8k_nzphr7m0q_.utils import *

@task_wrapper(task_id = "DatabricksPipeline_1")
def DatabricksPipeline_1(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "DatabricksPipeline_1",
        json = {"task_key" : "DatabricksPipeline_1"},
        databricks_conn_id = "",
    )
