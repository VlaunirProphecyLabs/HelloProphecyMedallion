from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def limit_10(spark: SparkSession, order_by_total_amount_desc_nulls_first: DataFrame) -> DataFrame:
    return order_by_total_amount_desc_nulls_first.limit(10)
