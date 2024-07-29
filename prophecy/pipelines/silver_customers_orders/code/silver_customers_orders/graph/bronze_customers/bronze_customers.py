from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from silver_customers_orders.udfs.UDFs import *
from . import *
from .config import *

def bronze_customers(spark: SparkSession, subgraph_config: SubgraphConfig) -> (DataFrame, DataFrame):
    Config.update(subgraph_config)
    df_bronze_customers_1 = bronze_customers_1(spark)
    df_silver_irs_zipcode_1 = silver_irs_zipcode_1(spark)
    df_add_sequence_column_1 = add_sequence_column_1(spark, df_silver_irs_zipcode_1)
    df_CustomerZipCodes_1 = CustomerZipCodes_1(spark, df_bronze_customers_1, df_add_sequence_column_1)
    subgraph_config.update(Config)

    return df_CustomerZipCodes_1, df_CustomerZipCodes_1
