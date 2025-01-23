from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.functions import *

def bronze_account_detail_table(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"`{Config.catalog_name}`.`helloworld_bronze`.`bronze_account_detail`")
