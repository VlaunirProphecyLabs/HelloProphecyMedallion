from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs import *

def gold_sales_by_zip_date(spark: SparkSession, in0: DataFrame):
    from pyspark.sql.utils import AnalysisException

    try:
        desc_table = spark.sql(
            "describe formatted {}".format(f"`{Config.catalog_name}`.`helloworld_gold`.`gold_sales_by_zip_date`")
        )
        table_exists = True
    except AnalysisException as e:
        table_exists = False

    if table_exists:
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"`{Config.catalog_name}`.`helloworld_gold`.`gold_sales_by_zip_date`")\
            .alias("target")\
            .merge(
              in0.alias("source"),
              (
                (col("source.zipcode") == col("target.zipcode"))
                & (col("source.order_date") == col("target.order_date"))
              )
            )\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write\
            .format("delta")\
            .mode("overwrite")\
            .saveAsTable(f"`{Config.catalog_name}`.`helloworld_gold`.`gold_sales_by_zip_date`")
