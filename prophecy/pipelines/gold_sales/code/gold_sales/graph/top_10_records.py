from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def top_10_records(spark: SparkSession, category_count_desc: DataFrame) -> DataFrame:
    return category_count_desc.limit(10)
