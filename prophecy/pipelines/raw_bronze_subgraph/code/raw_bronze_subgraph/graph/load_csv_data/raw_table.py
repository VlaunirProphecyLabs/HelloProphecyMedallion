from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

def raw_table(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable(f"`{Config.catalog_name}`.`helloworld_bronze`.`{Config.tablename}`")
