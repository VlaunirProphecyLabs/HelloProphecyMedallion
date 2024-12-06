from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from gold_sales.udfs import *

def SortByDateAndZip(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("order_date").asc(), col("zipcode").asc())
