from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_orders.config.ConfigStore import *
from silver_orders.udfs.UDFs import *

def by_order_id(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.order_id") == col("in1.order_id")), "inner")\
        .select(col("in0.order_id").alias("order_id"), col("in0.customer_id").alias("customer_id"), col("in0.order_status").alias("order_status"), col("in0.order_category").alias("order_category"), col("in0.order_date").alias("order_date"), col("in0.amount").alias("amount"), col("in1.item_name").alias("item_name"), col("in1.item_company").alias("item_company"), col("in1.quantity").alias("quantity"), col("in1.unit_price").alias("unit_price"), col("in1.shipping_address").alias("shipping_address"), col("in1.shipping_city").alias("shipping_city"), col("in1.shipping_state").alias("shipping_state"), col("in1.shipping_postal_code").alias("shipping_postal_code"), col("in1.payment_method").alias("payment_method"), col("in1.payment_status").alias("payment_status"), col("in1.shipping_status").alias("shipping_status"), col("in1.notes").alias("notes"))
