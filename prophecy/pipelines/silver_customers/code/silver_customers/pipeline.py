from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from silver_customers.config.ConfigStore import *
from silver_customers.udfs.UDFs import *
from prophecy.utils import *
from silver_customers.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_customers_1 = bronze_customers_1(spark)
    df_bronze_account_detail_table = bronze_account_detail_table(spark)
    df_irs_zipcodes_data = irs_zipcodes_data(spark, Config.irs_zipcodes_data)
    df_CustomerZipCodes_1 = CustomerZipCodes_1(
        spark, 
        df_bronze_customers_1, 
        df_bronze_account_detail_table, 
        df_irs_zipcodes_data
    )
    df_customers_reformatted = customers_reformatted(spark, df_CustomerZipCodes_1)
    silver_customers(spark, df_customers_reformatted)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver_customers")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/silver_customers", config = Config)(pipeline)

if __name__ == "__main__":
    main()
