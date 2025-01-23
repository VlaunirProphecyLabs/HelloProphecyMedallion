from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs import *

def orders_sorted_by_total(spark: SparkSession, total_orders_by_category: DataFrame) -> DataFrame:
    return total_orders_by_category.orderBy(col("TOTAL_ORDERS").desc())
