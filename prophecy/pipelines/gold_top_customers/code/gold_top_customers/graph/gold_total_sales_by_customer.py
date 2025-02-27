from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_top_customers.config.ConfigStore import *
from gold_top_customers.udfs import *

def gold_total_sales_by_customer(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"`{Config.catalog_name}`.`helloworld_gold`.`gold_total_sales_by_customer`")
