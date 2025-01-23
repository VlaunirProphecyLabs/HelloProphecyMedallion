from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs import *

def total_orders_by_category(spark: SparkSession, silver_order_customer_details: DataFrame) -> DataFrame:
    df1 = silver_order_customer_details.groupBy(col("order_category"))

    return df1.agg(count(lit(1)).alias("TOTAL_ORDERS"))
