from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from gold_sales.udfs import *
from . import *
from .config import *

def total_by_zip_and_date(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_deduplicate_by_order_id_zipcode_order_date_amount = deduplicate_by_order_id_zipcode_order_date_amount(spark, in0)
    df_TotalByZipCodeAndDate = TotalByZipCodeAndDate(spark, df_deduplicate_by_order_id_zipcode_order_date_amount)
    df_SortByDateAndZip = SortByDateAndZip(spark, df_TotalByZipCodeAndDate)
    subgraph_config.update(Config)

    return df_SortByDateAndZip
