from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers.config.ConfigStore import *
from silver_customers.udfs.UDFs import *

def CustomerZipCodes_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.customer_id") == col("in1.account_id")), "inner")\
        .join(in2.alias("in2"), (col("in1.billing_postal_code") == col("in2.zipcode")), "left_outer")\
        .select(col("in0.customer_id").alias("customer_id"), col("in0.first_name").alias("first_name"), col("in0.last_name").alias("last_name"), col("in0.phone").alias("phone"), col("in0.email").alias("email"), col("in0.country_code").alias("country_code"), col("in0.account_open_date").alias("account_open_date"), col("in0.account_flags").alias("account_flags"), col("in1.account_id").alias("account_id"), col("in1.account_name").alias("account_name"), col("in1.account_owner").alias("account_owner"), col("in1.phone_number").alias("phone_number"), col("in1.email").alias("billing_email"), col("in1.billing_address").alias("billing_address"), col("in1.billing_postal_code").alias("billing_postal_code"), col("in1.billing_city").alias("billing_city"), col("in1.billing_state").alias("billing_state"), col("in1.account_type").alias("account_type"), col("in1.industry").alias("industry"), col("in1.annual_revenue").alias("annual_revenue"), col("in1.number_of_employees").alias("number_of_employees"), col("in1.last_activity_date").alias("last_activity_date"), col("in1.created_date").alias("created_date"), col("in1.website").alias("website"), col("in1.lead_source").alias("lead_source"), col("in1.status").alias("status"), col("in1.rating").alias("rating"), col("in1.description").alias("description"), col("in1.last_modified_by").alias("last_modified_by"), col("in1.last_modified_date").alias("last_modified_date"), col("in2.zipcode").alias("zipcode"), col("in2.state").alias("state"), col("in2.high_income_percent").alias("high_income_percent"), col("in2.high_income_returns").alias("high_income_returns"), col("in2.low_income_returns").alias("low_income_returns"), col("in2.all_returns").alias("all_returns"), col("in2.is_high_income").alias("is_high_income"))
