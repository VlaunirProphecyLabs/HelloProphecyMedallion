from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze.config.ConfigStore import *
from raw_bronze.udfs import *

def order_item_detail(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", StringType(), True), StructField("item_name", StringType(), True), StructField("item_company", StringType(), True), StructField("quantity", StringType(), True), StructField("unit_price", StringType(), True), StructField("order_date", StringType(), True), StructField("shipping_address", StringType(), True), StructField("shipping_city", StringType(), True), StructField("shipping_state", StringType(), True), StructField("shipping_postal_code", StringType(), True), StructField("payment_method", StringType(), True), StructField("payment_status", StringType(), True), StructField("shipping_status", StringType(), True), StructField("notes", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("multiLine", True)\
        .csv("dbfs:/Users/vlaunir@prophecy.io/delimited/item_detail.csv")
