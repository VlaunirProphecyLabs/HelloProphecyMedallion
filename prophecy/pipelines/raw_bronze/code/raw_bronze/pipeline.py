from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from raw_bronze.config.ConfigStore import *
from raw_bronze.udfs import *
from prophecy.utils import *
from raw_bronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_account_detail = raw_account_detail(spark)
    df_ReformatCustomers_1 = ReformatCustomers_1(spark, df_raw_account_detail)
    df_raw_orders = raw_orders(spark)
    df_raw_irs_zipcode = raw_irs_zipcode(spark)
    df_ReformatIRS = ReformatIRS(spark, df_raw_irs_zipcode)
    bronze_account_detail_table(spark, df_ReformatCustomers_1)
    df_ReformatOrders = ReformatOrders(spark, df_raw_orders)
    df_order_item_detail = order_item_detail(spark)
    df_Reformat_1 = Reformat_1(spark, df_order_item_detail)
    bronze_order_detail(spark, df_Reformat_1)
    df_raw_customers = raw_customers(spark)
    df_ReformatCustomers = ReformatCustomers(spark, df_raw_customers)
    bronze_orders(spark, df_ReformatOrders)
    bronze_customers(spark, df_ReformatCustomers)
    bronze_irs_zipcode(spark, df_ReformatIRS)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/raw_bronze")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/raw_bronze", config = Config)(pipeline)

if __name__ == "__main__":
    main()
