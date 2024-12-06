from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_orders.config.ConfigStore import *
from silver_orders.udfs import *

def reformat_order_details(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("order_id"), 
        col("customer_id"), 
        col("order_status"), 
        col("order_category"), 
        col("order_date"), 
        col("amount"), 
        col("item_name"), 
        col("item_company"), 
        col("quantity"), 
        col("unit_price"), 
        col("shipping_address"), 
        col("shipping_city"), 
        col("shipping_state"), 
        col("shipping_postal_code"), 
        col("payment_method"), 
        col("payment_status"), 
        col("shipping_status"), 
        col("notes")
    )
