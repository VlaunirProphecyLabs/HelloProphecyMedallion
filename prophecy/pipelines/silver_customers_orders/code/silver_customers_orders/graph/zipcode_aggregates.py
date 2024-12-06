from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs import *

def zipcode_aggregates(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("zipcode"))

    return df1.agg(
        sum(col("all_returns")).alias("total_returns"), 
        (sum(col("high_income_returns")) / col("total_returns")).alias("high_income_return_ratio"), 
        (sum(col("low_income_returns")) / col("total_returns")).alias("low_income_return_ratio"), 
        avg(col("high_income_returns")).alias("avg_high_income_percent"), 
        avg(col("low_income_returns")).alias("avg_low_income_percent")
    )
