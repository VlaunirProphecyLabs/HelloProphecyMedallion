from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs.UDFs import *

def bronze_orders(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"scottdemo.bronze_orders")