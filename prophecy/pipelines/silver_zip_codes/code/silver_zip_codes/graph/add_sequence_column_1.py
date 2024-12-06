from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_zip_codes.config.ConfigStore import *
from silver_zip_codes.udfs import *

def add_sequence_column_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("customer_name", lit("abc"))\
        .withColumn("customer_id", row_number().over(Window.partitionBy(col("customer_name")).orderBy(col("customer_name").asc())))\
        .drop("customer_name")
