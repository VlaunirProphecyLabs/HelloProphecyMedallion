from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs import *
from prophecy.utils import *
from silver_customers_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_orders = silver_orders(spark)
    df_silver_irs_zipcode = silver_irs_zipcode(spark)
    df_zipcode_aggregates = zipcode_aggregates(spark, df_silver_irs_zipcode)
    df_silver_customers = silver_customers(spark)
    df_Filter_1 = Filter_1(spark, df_silver_customers)
    df_inner_join_by_customer_id = inner_join_by_customer_id(
        spark, 
        df_Filter_1, 
        df_silver_orders, 
        df_zipcode_aggregates
    )
    df_customer_details_reformat = customer_details_reformat(spark, df_inner_join_by_customer_id)
    silver_order_customer_details(spark, df_customer_details_reformat)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver_customers_orders")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/silver_customers_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
