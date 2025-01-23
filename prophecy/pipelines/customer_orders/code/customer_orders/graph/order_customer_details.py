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
        .select(col("bronze_orders.order_id").alias("order_id"), col("bronze_orders.customer_id").alias("customer_id"), col("bronze_orders.order_status").alias("order_status"), col("bronze_orders.order_category").alias("order_category"), col("bronze_orders.order_date").alias("order_date"), col("bronze_orders.amount").alias("amount"), col("bronze_customers.first_name").alias("first_name"), col("bronze_customers.last_name").alias("last_name"), col("bronze_customers.phone").alias("phone"), col("bronze_customers.email").alias("email"), col("bronze_customers.country_code").alias("country_code"), col("bronze_customers.account_open_date").alias("account_open_date"), col("bronze_customers.account_flags").alias("account_flags"))
