from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *

@instrument
def add_load_date(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("updated_at", from_utc_timestamp(current_timestamp(), "America/New_York"))
