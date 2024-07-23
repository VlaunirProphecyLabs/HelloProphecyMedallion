from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

def read_dynamic_source(spark: SparkSession) -> DataFrame:
    from pyspark.sql import *
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from prophecy.utils import *
    from prophecy.libs import typed_lit
    #from raw_bronze_subgraph.config.ConfigStore import *
    #from raw_bronze_subgraph.functions import *
    file_name = Config.source_path
    out0 = spark.read.option("header", True).option("inferSchema", True).option("sep", ",").csv(file_name)

    return out0
