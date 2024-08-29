from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_orders.config.ConfigStore import *
from silver_orders.udfs.UDFs import *

def silver_orders(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .partitionBy("order_date")\
        .saveAsTable(f"`{Config.catalog_name}`.`helloworld_silver`.`silver_orders`")
