from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def aggregate_details(spark: SparkSession, customer_order_summary: DataFrame) -> DataFrame:
    return customer_order_summary.select(
        col("CUSTOMER_ID"), 
        col("FIRST_NAME"), 
        col("LAST_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("ZIPCODE"), 
        col("ACCOUNT_OPEN_DATE"), 
        col("ACCOUNT_FLAGS"), 
        col("TOTAL_ORDERS"), 
        col("TOTAL_AMOUNT"), 
        col("AVERAGE_AMOUNT"), 
        col("LAST_ORDER_DATE"), 
        col("FIRST_ORDER_DATE"), 
        rand_zip_index(col("ZIPCODE").cast(IntegerType())).alias("ZIP_INDEX")
    )
