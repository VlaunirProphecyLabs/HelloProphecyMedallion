from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs import *

def silver_customers(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"`{Config.catalog_name}`.`helloworld_silver`.`silver_customers`")
