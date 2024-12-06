from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *

@instrument
def gen_source_files(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("tablename", StringType(), True), StructField("source_path", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv(Config.source_files_path)
