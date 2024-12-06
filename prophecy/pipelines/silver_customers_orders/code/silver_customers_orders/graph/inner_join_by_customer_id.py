from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs import *

def inner_join_by_customer_id(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in1.customer_id") == col("in0.customer_id")), "inner")\
        .join(in2.alias("in2"), (col("in0.billing_postal_code") == col("in2.zipcode")), "left_outer")\
        .select(col("in0.customer_id").alias("customer_id"), col("in0.first_name").alias("first_name"), col("in0.last_name").alias("last_name"), col("in0.phone").alias("phone"), col("in0.email").alias("email"), col("in0.country_code").alias("country_code"), col("in0.account_open_date").alias("account_open_date"), col("in0.account_flags").alias("account_flags"), col("in0.account_id").alias("account_id"), col("in0.account_name").alias("account_name"), col("in0.account_owner").alias("account_owner"), col("in0.phone_number").alias("phone_number"), col("in0.billing_address").alias("billing_address"), col("in0.billing_postal_code").alias("billing_postal_code"), col("in0.billing_city").alias("billing_city"), col("in0.billing_state").alias("billing_state"), col("in0.billing_email").alias("billing_email"), col("in0.account_type").alias("account_type"), col("in0.industry").alias("industry"), col("in0.annual_revenue").alias("annual_revenue"), col("in0.number_of_employees").alias("number_of_employees"), col("in0.last_activity_date").alias("last_activity_date"), col("in0.created_date").alias("created_date"), col("in0.website").alias("website"), col("in0.lead_source").alias("lead_source"), col("in0.status").alias("status"), col("in0.rating").alias("rating"), col("in0.description").alias("description"), col("in0.last_modified_by").alias("last_modified_by"), col("in0.last_modified_date").alias("last_modified_date"), col("in0.zipcode").alias("zipcode"), col("in0.state").alias("state"), col("in0.high_income_percent").alias("high_income_percent"), col("in0.high_income_returns").alias("high_income_returns"), col("in0.low_income_returns").alias("low_income_returns"), col("in0.all_returns").alias("all_returns"), col("in0.is_high_income").alias("is_high_income"), col("in1.order_id").alias("order_id"), col("in1.order_status").alias("order_status"), col("in1.order_category").alias("order_category"), col("in1.order_date").alias("order_date"), col("in1.amount").alias("amount"), col("in1.item_name").alias("item_name"), col("in1.item_company").alias("item_company"), col("in1.quantity").alias("quantity"), col("in1.unit_price").alias("unit_price"), col("in1.shipping_address").alias("shipping_address"), col("in1.shipping_city").alias("shipping_city"), col("in1.shipping_state").alias("shipping_state"), col("in1.shipping_postal_code").alias("shipping_postal_code"), col("in1.payment_method").alias("payment_method"), col("in1.payment_status").alias("payment_status"), col("in1.shipping_status").alias("shipping_status"), col("in1.notes").alias("notes"))
