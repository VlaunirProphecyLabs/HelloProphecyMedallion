from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def by_email_account_name(
        spark: SparkSession,
        bronze_account_detail_table: DataFrame,
        bronze_demo_customer: DataFrame,
) -> DataFrame:
    return bronze_account_detail_table\
        .alias("bronze_account_detail_table")\
        .join(
          bronze_demo_customer.alias("bronze_demo_customer"),
          (
            ((col("bronze_account_detail_table.account_id") == col("bronze_demo_customer.account_open_date")) & (col("bronze_account_detail_table.account_name") == col("bronze_demo_customer.account_flags")))
            & (col("bronze_account_detail_table.email") == col("bronze_demo_customer.email"))
          ),
          "inner"
        )\
        .select(col("bronze_demo_customer.customer_id").alias("customer_id"), col("bronze_demo_customer.first_name").alias("first_name"), col("bronze_demo_customer.last_name").alias("last_name"), col("bronze_demo_customer.phone").alias("phone"), col("bronze_demo_customer.country_code").alias("country_code"), col("bronze_account_detail_table.account_owner").alias("account_owner"), col("bronze_account_detail_table.account_id").alias("account_id"), col("bronze_account_detail_table.billing_address").alias("billing_address"), col("bronze_account_detail_table.industry").alias("industry"), col("bronze_account_detail_table.phone_number").alias("phone_number"), col("bronze_account_detail_table.billing_city").alias("billing_city"), col("bronze_account_detail_table.lead_source").alias("lead_source"), col("bronze_account_detail_table.number_of_employees").alias("number_of_employees"), col("bronze_account_detail_table.status").alias("status"), col("bronze_account_detail_table.website").alias("website"), col("bronze_account_detail_table.email").alias("email"), col("bronze_account_detail_table.annual_revenue").alias("annual_revenue"), col("bronze_account_detail_table.billing_state").alias("billing_state"), col("bronze_account_detail_table.description").alias("description"), col("bronze_account_detail_table.rating").alias("rating"), col("bronze_account_detail_table.last_modified_by").alias("last_modified_by"), col("bronze_account_detail_table.account_name").alias("account_name"), col("bronze_account_detail_table.billing_postal_code").alias("billing_postal_code"), col("bronze_account_detail_table.last_activity_date").alias("last_activity_date"), col("bronze_account_detail_table.account_type").alias("account_type"), col("bronze_account_detail_table.last_modified_date").alias("last_modified_date"), col("bronze_account_detail_table.created_date").alias("created_date"))
