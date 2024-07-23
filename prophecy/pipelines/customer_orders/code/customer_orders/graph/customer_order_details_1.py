from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def customer_order_details_1(spark: SparkSession, customer_order_details: DataFrame) -> DataFrame:
    return customer_order_details.select(
        col("CUSTOMER_ID"), 
        col("FIRST_NAME"), 
        col("LAST_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("ZIPCODE"), 
        col("ACCOUNT_OPEN_DATE"), 
        col("ACCOUNT_FLAGS"), 
        col("ORDER_ID"), 
        col("ORDER_STATUS"), 
        col("ORDER_CATEGORY"), 
        col("ORDER_DATE"), 
        col("AMOUNT"), 
        datediff(lit("CURRENT_DATE"), col("ACCOUNT_OPEN_DATE")).alias("ACCOUNT_AGE"), 
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("full_name"), 
        when(((col("AMOUNT") >= lit(5000)) & (col("AMOUNT") <= lit(10000))), lit(1))\
          .otherwise(lit(0))\
          .alias("flag_transactions")
    )
