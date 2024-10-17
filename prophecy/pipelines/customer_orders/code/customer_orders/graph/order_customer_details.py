from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def order_customer_details(spark: SparkSession, silver_orders: DataFrame, silver_customers: DataFrame, ) -> DataFrame:
    return silver_orders\
        .alias("silver_orders")\
        .join(
          silver_customers.alias("silver_customers"),
          (col("silver_orders.customer_id") == col("silver_customers.customer_id")),
          "inner"
        )\
        .select(col("silver_orders.order_id").alias("ORDER_ID"), col("silver_orders.customer_id").alias("CUSTOMER_ID"), col("silver_orders.order_status").alias("ORDER_STATUS"), col("silver_orders.order_category").alias("ORDER_CATEGORY"), col("silver_orders.order_date").alias("ORDER_DATE"), col("silver_orders.amount").alias("AMOUNT"), col("silver_orders.item_name").alias("ITEM_NAME"), col("silver_orders.item_company").alias("ITEM_COMPANY"), col("silver_orders.quantity").alias("QUANTITY"), col("silver_orders.unit_price").alias("UNIT_PRICE"), col("silver_orders.shipping_address").alias("SHIPPING_ADDRESS"), col("silver_orders.shipping_city").alias("SHIPPING_CITY"), col("silver_orders.shipping_state").alias("SHIPPING_STATE"), col("silver_orders.shipping_postal_code").alias("SHIPPING_POSTAL_CODE"), col("silver_orders.payment_method").alias("PAYMENT_METHOD"), col("silver_orders.payment_status").alias("PAYMENT_STATUS"), col("silver_orders.shipping_status").alias("SHIPPING_STATUS"), col("silver_orders.notes").alias("NOTES"), col("silver_customers.first_name").alias("FIRST_NAME"), col("silver_customers.last_name").alias("LAST_NAME"), col("silver_customers.phone").alias("PHONE"), col("silver_customers.email").alias("EMAIL"), col("silver_customers.billing_address").alias("BILLING_ADDRESS"), col("silver_customers.billing_postal_code").alias("BILLING_POSTAL_CODE"), col("silver_customers.billing_city").alias("BILLING_CITY"), col("silver_customers.billing_state").alias("BILLING_STATE"), col("silver_customers.billing_email").alias("BILLING_EMAIL"), col("silver_customers.industry").alias("INDUSTRY"), col("silver_customers.annual_revenue").alias("ANNUAL_REVENUE"), col("silver_customers.number_of_employees").alias("NUMBER_OF_EMPLOYEES"), col("silver_customers.website").alias("WEBSITE"), col("silver_customers.status").alias("STATUS"), col("silver_customers.rating").alias("RATING"), col("silver_customers.description").alias("DESCRIPTION"), col("silver_customers.last_modified_by").alias("LAST_MODIFIED_BY"), col("silver_customers.state").alias("STATE"), col("silver_customers.all_returns").alias("ALL_RETURNS"))
