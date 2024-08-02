from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def order_customer_details(spark: SparkSession, bronze_orders: DataFrame, bronze_customers: DataFrame, ) -> DataFrame:
    return bronze_orders\
        .alias("bronze_orders")\
        .join(
          bronze_customers.alias("bronze_customers"),
          (col("bronze_orders.customer_id") == col("bronze_customers.customer_id")),
          "inner"
        )\
        .select(col("bronze_orders.order_id").alias("ORDER_ID"), col("bronze_orders.customer_id").alias("CUSTOMER_ID"), col("bronze_orders.order_status").alias("ORDER_STATUS"), col("bronze_orders.order_category").alias("ORDER_CATEGORY"), col("bronze_orders.order_date").alias("ORDER_DATE"), col("bronze_orders.amount").alias("AMOUNT"), col("bronze_customers.first_name").alias("FIRST_NAME"), col("bronze_customers.last_name").alias("LAST_NAME"), col("bronze_customers.phone").alias("PHONE"), col("bronze_customers.email").alias("EMAIL"), col("bronze_customers.country_code").alias("COUNTRY_CODE"), col("bronze_customers.account_open_date").alias("ACCOUNT_OPEN_DATE"), col("bronze_customers.account_flags").alias("ACCOUNT_FLAGS"), col("bronze_customers.full_name").alias("FULL_NAME"))
