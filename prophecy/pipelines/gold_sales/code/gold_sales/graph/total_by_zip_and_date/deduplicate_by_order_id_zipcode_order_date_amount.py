from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from gold_sales.udfs import *

def deduplicate_by_order_id_zipcode_order_date_amount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["order_id", "zipcode", "order_date", "amount"])
