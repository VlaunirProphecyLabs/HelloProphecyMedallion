from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def silver_customers(spark: SparkSession) -> DataFrame:
    return spark.read.table("`scottdemo`.`silver_customers`")
