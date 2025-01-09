from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def customer_order_details(spark: SparkSession, bronze_customers: DataFrame, bronze_orders: DataFrame, ) -> DataFrame:
    return bronze_customers\
        .alias("bronze_customers")\
        .join(
          bronze_orders.alias("bronze_orders"),
          (col("bronze_customers.customer_id") == col("bronze_orders.customer_id")),
          "inner"
        )\
        .select(col("bronze_customers.customer_id").alias("customer_id"), col("bronze_customers.first_name").alias("first_name"), col("bronze_customers.last_name").alias("last_name"), col("bronze_customers.phone").alias("phone"), col("bronze_customers.email").alias("email"), col("bronze_orders.order_id").alias("order_id"), col("bronze_orders.order_status").alias("order_status"), col("bronze_orders.order_category").alias("order_category"), col("bronze_orders.order_date").alias("order_date"), col("bronze_orders.amount").alias("amount"))
