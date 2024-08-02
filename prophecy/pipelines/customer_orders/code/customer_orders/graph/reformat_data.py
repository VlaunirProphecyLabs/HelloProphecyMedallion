from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def reformat_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("ORDER_ID"), 
        col("CUSTOMER_ID"), 
        col("ORDER_STATUS"), 
        col("ORDER_CATEGORY"), 
        col("ORDER_DATE"), 
        col("AMOUNT"), 
        col("FIRST_NAME"), 
        col("LAST_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("COUNTRY_CODE"), 
        col("ACCOUNT_OPEN_DATE"), 
        col("ACCOUNT_FLAGS"), 
        col("FULL_NAME"), 
        datediff(current_date(), to_date(col("ACCOUNT_OPEN_DATE"))).alias("account_age"), 
        upper(col("FULL_NAME")).alias("capital_full_name"), 
        when(((col("AMOUNT") >= lit(5000)) & (col("AMOUNT") <= lit(10000))), lit(1))\
          .otherwise(lit(0))\
          .alias("amount_flag"), 
        when(month(to_date(col("ORDER_DATE"))).isin(lit(12), lit(1), lit(2)), lit("Winter"))\
          .when(month(to_date(col("ORDER_DATE"))).isin(lit(3), lit(4), lit(5)), lit("Spring"))\
          .when(month(to_date(col("ORDER_DATE"))).isin(lit(6), lit(7), lit(8)), lit("Summer"))\
          .when(month(to_date(col("ORDER_DATE"))).isin(lit(9), lit(10), lit(11)), lit("Fall"))\
          .otherwise(lit("Unknown"))\
          .alias("order_season")
    )
