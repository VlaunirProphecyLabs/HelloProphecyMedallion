from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def customer_order_details(spark: SparkSession, silver_customers: DataFrame, silver_orders: DataFrame, ) -> DataFrame:
    return silver_customers\
        .alias("silver_customers")\
        .join(
          silver_orders.alias("silver_orders"),
          (col("silver_customers.customer_id") == col("silver_orders.customer_id")),
          "inner"
        )\
        .select(col("silver_customers.customer_id").alias("CUSTOMER_ID"), col("silver_customers.first_name").alias("FIRST_NAME"), col("silver_customers.last_name").alias("LAST_NAME"), col("silver_customers.phone").alias("PHONE"), col("silver_customers.email").alias("EMAIL"), col("silver_customers.zipcode").alias("ZIPCODE"), col("silver_customers.account_open_date").alias("ACCOUNT_OPEN_DATE"), col("silver_customers.account_flags").alias("ACCOUNT_FLAGS"), col("silver_orders.order_id").alias("ORDER_ID"), col("silver_orders.order_status").alias("ORDER_STATUS"), col("silver_orders.order_category").alias("ORDER_CATEGORY"), col("silver_orders.order_date").alias("ORDER_DATE"), col("silver_orders.amount").alias("AMOUNT"))
