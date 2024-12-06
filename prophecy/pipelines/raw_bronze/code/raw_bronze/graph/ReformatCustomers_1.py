from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze.config.ConfigStore import *
from raw_bronze.udfs import *

def ReformatCustomers_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("account_id"), 
        col("account_name"), 
        col("account_owner"), 
        col("phone_number"), 
        col("email"), 
        col("billing_address"), 
        col("billing_postal_code"), 
        col("billing_city"), 
        col("billing_state"), 
        col("account_type"), 
        col("industry"), 
        col("annual_revenue"), 
        col("number_of_employees"), 
        col("last_activity_date"), 
        col("created_date"), 
        col("website"), 
        col("lead_source"), 
        col("status"), 
        col("rating"), 
        col("description"), 
        col("last_modified_by"), 
        col("last_modified_date")
    )
