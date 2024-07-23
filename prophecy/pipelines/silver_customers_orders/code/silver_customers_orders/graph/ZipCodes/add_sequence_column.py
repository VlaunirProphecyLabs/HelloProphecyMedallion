from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from silver_customers_orders.udfs.UDFs import *

def add_sequence_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("customer_name", lit("abc"))\
        .withColumn("customer_id", row_number().over(Window.partitionBy(col("customer_name")).orderBy(col("customer_name").asc())))\
        .drop("customer_name")
