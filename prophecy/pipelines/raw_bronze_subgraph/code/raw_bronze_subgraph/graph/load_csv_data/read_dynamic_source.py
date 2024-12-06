from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

@instrument
def read_dynamic_source(spark: SparkSession) -> DataFrame:
    
    file_name = Config.source_path
    out0 = spark.read\
               .option("header", True)\
               .option("inferSchema", True)\
               .option("multiLine", True)\
               .option("sep", ",")\
               .csv(file_name)

    return out0
