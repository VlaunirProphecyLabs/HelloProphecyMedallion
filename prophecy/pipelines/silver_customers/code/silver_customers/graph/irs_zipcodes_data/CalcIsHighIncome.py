from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from silver_customers.udfs import *

@instrument
def CalcIsHighIncome(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("zipcode"), 
        col("state"), 
        ((lit(100) * col("high_income_returns")) / col("all_returns")).alias("high_income_percent"), 
        col("high_income_returns"), 
        col("low_income_returns"), 
        col("all_returns"), 
        ((col("high_income_returns") / col("all_returns")) > lit(0.1)).alias("is_high_income")
    )
