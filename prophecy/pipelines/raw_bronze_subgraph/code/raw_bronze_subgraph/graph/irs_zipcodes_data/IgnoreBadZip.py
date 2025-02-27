from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

@instrument
def IgnoreBadZip(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        (((col("zipcode") != lit("00000")) & (col("zipcode") != lit("99999"))) & col("zipcode").isNotNull())
    )
