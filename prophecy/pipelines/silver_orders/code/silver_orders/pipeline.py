from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from silver_orders.config.ConfigStore import *
from silver_orders.udfs.UDFs import *
from prophecy.utils import *
from silver_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_orders = bronze_orders(spark)
    df_bronze_order_detail = bronze_order_detail(spark)
    df_by_order_id = by_order_id(spark, df_bronze_orders, df_bronze_order_detail)
    df_reformat_order_details = reformat_order_details(spark, df_by_order_id)
    silver_orders(spark, df_reformat_order_details)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver_orders")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/silver_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
