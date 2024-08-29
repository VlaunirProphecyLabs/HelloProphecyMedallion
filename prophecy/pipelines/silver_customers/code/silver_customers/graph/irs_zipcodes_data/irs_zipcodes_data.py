from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from silver_customers.udfs.UDFs import *
from . import *
from .config import *

def irs_zipcodes_data(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_bronze_irs_zipcode = bronze_irs_zipcode(spark)
    df_IgnoreBadZip = IgnoreBadZip(spark, df_bronze_irs_zipcode)
    df_CastDataTypes = CastDataTypes(spark, df_IgnoreBadZip)
    df_SumIncomeBracketsByZip = SumIncomeBracketsByZip(spark, df_CastDataTypes)
    df_CalcIsHighIncome = CalcIsHighIncome(spark, df_SumIncomeBracketsByZip)
    subgraph_config.update(Config)

    return df_CalcIsHighIncome
