from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def create_regions(country_code: Column=lambda: col("country_code")):
    return when((country_code == lit("US")), lit("North America"))\
        .when((country_code == lit("CA")), lit("North America"))\
        .when((country_code == lit("MX")), lit("North America"))\
        .when((country_code == lit("BR")), lit("South America"))\
        .when((country_code == lit("UK")), lit("Europe"))\
        .otherwise(lit("Other"))\
        .alias("country_region")

@execute_rule
def client_tier(country_code: Column=lambda: col("country_code"), account_flags: Column=lambda: col("account_flags")):
    return when((country_code.isin(lit("US"), lit("CA"), lit("MX")) & (account_flags == lit("A"))), lit("Level 1"))\
        .when((country_code.isin(lit("BR"), lit("UK")) & (account_flags == lit("F"))), lit("Level 2"))\
        .otherwise(lit("Level 0"))\
        .alias("customer_level")

@execute_rule
def demo(country_code: Column=lambda: col("country_code")):
    return when(country_code.isin(lit("US"), lit("CA"), lit("MX")), lit("North America"))\
        .when((country_code == lit("BR")), lit("South Americe"))\
        .otherwise(lit("Other"))\
        .alias("country_region_demo")
