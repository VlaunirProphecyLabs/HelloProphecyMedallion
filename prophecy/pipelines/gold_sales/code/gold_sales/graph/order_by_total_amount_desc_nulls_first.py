from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def order_by_total_amount_desc_nulls_first(spark: SparkSession, customer_order_total: DataFrame) -> DataFrame:
    return customer_order_total.orderBy(col("TOTAL_AMOUNT").desc())
