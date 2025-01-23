from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

@instrument
def raw_dynamic_source(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", ",")\
        .option("multiLine", True)\
        .csv(Config.source_path)
