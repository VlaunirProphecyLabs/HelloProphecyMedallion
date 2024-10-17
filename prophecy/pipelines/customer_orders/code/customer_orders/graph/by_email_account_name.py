from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def by_email_account_name(
        spark: SparkSession,
        raw_account_detail: DataFrame,
        bronze_customers: DataFrame,
) -> DataFrame:
    return raw_account_detail\
        .alias("raw_account_detail")\
        .join(
          bronze_customers.alias("bronze_customers"),
          (
            ((col("raw_account_detail.account_name") == col("bronze_customers.account_flags")) & (col("raw_account_detail.email") == col("bronze_customers.email")))
            & (col("raw_account_detail.phone_number") == col("bronze_customers.phone"))
          ),
          "inner"
        )\
        .select(col("bronze_customers.customer_id").alias("customer_id"), col("bronze_customers.first_name").alias("first_name"), col("bronze_customers.last_name").alias("last_name"), col("bronze_customers.country_code").alias("country_code"), col("bronze_customers.account_open_date").alias("account_open_date"), col("bronze_customers.full_name").alias("full_name"), col("raw_account_detail.status").alias("status"), col("raw_account_detail.description").alias("description"), col("raw_account_detail.last_modified_by").alias("last_modified_by"), col("raw_account_detail.annual_revenue").alias("annual_revenue"), col("raw_account_detail.last_activity_date").alias("last_activity_date"), col("raw_account_detail.number_of_employees").alias("number_of_employees"), col("raw_account_detail.account_type").alias("account_type"), col("raw_account_detail.website").alias("website"), col("raw_account_detail.rating").alias("rating"), col("raw_account_detail.billing_postal_code").alias("billing_postal_code"), col("raw_account_detail.lead_source").alias("lead_source"), col("raw_account_detail.industry").alias("industry"), col("raw_account_detail.email").alias("email"), col("raw_account_detail.created_date").alias("created_date"), col("raw_account_detail.billing_city").alias("billing_city"), col("raw_account_detail.account_id").alias("account_id"), col("raw_account_detail.account_name").alias("account_name"), col("raw_account_detail.billing_state").alias("billing_state"), col("raw_account_detail.last_modified_date").alias("last_modified_date"), col("raw_account_detail.billing_address").alias("billing_address"), col("raw_account_detail.account_owner").alias("account_owner"), col("raw_account_detail.phone_number").alias("phone_number"))
