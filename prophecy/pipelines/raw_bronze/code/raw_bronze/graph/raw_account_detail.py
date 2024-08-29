from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze.config.ConfigStore import *
from raw_bronze.udfs.UDFs import *

def raw_account_detail(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("account_id", StringType(), True), StructField("account_name", StringType(), True), StructField("account_owner", StringType(), True), StructField("phone_number", StringType(), True), StructField("email", StringType(), True), StructField("billing_address", StringType(), True), StructField("billing_postal_code", StringType(), True), StructField("billing_city", StringType(), True), StructField("billing_state", StringType(), True), StructField("account_type", StringType(), True), StructField("industry", StringType(), True), StructField("annual_revenue", StringType(), True), StructField("number_of_employees", StringType(), True), StructField("last_activity_date", StringType(), True), StructField("created_date", StringType(), True), StructField("website", StringType(), True), StructField("lead_source", StringType(), True), StructField("status", StringType(), True), StructField("rating", StringType(), True), StructField("description", StringType(), True), StructField("last_modified_by", StringType(), True), StructField("last_modified_date", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("multiLine", True)\
        .csv("dbfs:/Users/vlaunir@prophecy.io/delimited/account_detail.csv")
