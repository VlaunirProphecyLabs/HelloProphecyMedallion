from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs import *

def deduplicate_customers(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["customer_id", "first_name", "last_name"])
