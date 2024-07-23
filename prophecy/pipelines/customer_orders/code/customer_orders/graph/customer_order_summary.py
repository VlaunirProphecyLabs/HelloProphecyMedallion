from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def customer_order_summary(spark: SparkSession, customer_order_details_1: DataFrame) -> DataFrame:
    df1 = customer_order_details_1.groupBy(
        col("CUSTOMER_ID"), 
        col("FIRST_NAME"), 
        col("LAST_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("ZIPCODE"), 
        col("ACCOUNT_OPEN_DATE"), 
        col("ACCOUNT_FLAGS")
    )

    return df1.agg(
        countDistinct(col("ORDER_ID")).alias("TOTAL_ORDERS"), 
        sum(col("AMOUNT")).alias("TOTAL_AMOUNT"), 
        avg(col("AMOUNT")).alias("AVERAGE_AMOUNT"), 
        max(col("ORDER_DATE")).alias("LAST_ORDER_DATE"), 
        min(col("ORDER_DATE")).alias("FIRST_ORDER_DATE")
    )
