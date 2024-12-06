from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

@instrument
def add_updated_at_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("updated_at", lit(Config.updated_at))
