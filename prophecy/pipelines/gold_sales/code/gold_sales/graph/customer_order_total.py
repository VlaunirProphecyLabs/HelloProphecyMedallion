from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def customer_order_total(spark: SparkSession, silver_order_customer_details: DataFrame) -> DataFrame:
    df1 = silver_order_customer_details.groupBy(col("customer_id"), col("first_name"), col("last_name"))

    return df1.agg(sum(col("amount")).alias("TOTAL_AMOUNT"))
