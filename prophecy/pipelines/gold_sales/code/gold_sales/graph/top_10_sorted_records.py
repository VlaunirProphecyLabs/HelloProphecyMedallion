from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs import *

def top_10_sorted_records(spark: SparkSession, orders_sorted_by_total: DataFrame) -> DataFrame:
    return orders_sorted_by_total.limit(10)
