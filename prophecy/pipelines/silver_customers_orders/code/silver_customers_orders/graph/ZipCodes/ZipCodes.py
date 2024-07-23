from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from silver_customers_orders.udfs.UDFs import *
from . import *
from .config import *

def ZipCodes(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_silver_irs_zipcode = silver_irs_zipcode(spark)
    df_add_sequence_column = add_sequence_column(spark, df_silver_irs_zipcode)
    subgraph_config.update(Config)

    return df_add_sequence_column
