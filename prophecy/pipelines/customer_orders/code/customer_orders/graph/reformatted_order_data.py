from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def reformatted_order_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("ORDER_ID"), 
        col("CUSTOMER_ID"), 
        col("ORDER_STATUS"), 
        col("ORDER_CATEGORY"), 
        col("ORDER_DATE"), 
        col("AMOUNT"), 
        col("ITEM_NAME"), 
        col("ITEM_COMPANY"), 
        col("QUANTITY"), 
        col("UNIT_PRICE"), 
        col("SHIPPING_ADDRESS"), 
        col("SHIPPING_CITY"), 
        col("SHIPPING_STATE"), 
        col("SHIPPING_POSTAL_CODE"), 
        col("PAYMENT_METHOD"), 
        col("PAYMENT_STATUS"), 
        col("SHIPPING_STATUS"), 
        col("NOTES"), 
        col("FIRST_NAME"), 
        col("LAST_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("BILLING_ADDRESS"), 
        col("BILLING_POSTAL_CODE"), 
        col("BILLING_CITY"), 
        col("BILLING_STATE"), 
        col("BILLING_EMAIL"), 
        col("INDUSTRY"), 
        col("ANNUAL_REVENUE"), 
        col("NUMBER_OF_EMPLOYEES"), 
        col("WEBSITE"), 
        col("STATUS"), 
        col("RATING"), 
        col("DESCRIPTION"), 
        col("LAST_MODIFIED_BY"), 
        col("STATE"), 
        col("ALL_RETURNS"), 
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("full_name"), 
        datediff(current_date(), to_date(col("ORDER_DATE"))).alias("account_age"), 
        when((col("AMOUNT") > lit(10000)), lit("Flagged")).otherwise(lit("Not Flagged")).alias("transaction_flag"), 
        when(month(to_date(col("ORDER_DATE"))).isin(lit(12), lit(1), lit(2)), lit("Winter"))\
          .when(month(to_date(col("ORDER_DATE"))).isin(lit(3), lit(4), lit(5)), lit("Spring"))\
          .when(month(to_date(col("ORDER_DATE"))).isin(lit(6), lit(7), lit(8)), lit("Summer"))\
          .otherwise(lit("Fall"))\
          .alias("season")
    )
