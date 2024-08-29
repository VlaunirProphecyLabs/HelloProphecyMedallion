from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers.config.ConfigStore import *
from silver_customers.udfs.UDFs import *

def customers_reformatted(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags"), 
        col("account_id"), 
        col("account_name"), 
        col("account_owner"), 
        col("phone_number"), 
        col("billing_address"), 
        col("billing_postal_code"), 
        col("billing_city"), 
        col("billing_state"), 
        col("billing_email"), 
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
        col("last_modified_date"), 
        col("zipcode"), 
        col("state"), 
        col("high_income_percent"), 
        col("high_income_returns"), 
        col("low_income_returns"), 
        col("all_returns"), 
        col("is_high_income")
    )