from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *
from prophecy.utils import *
from gold_sales.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_order_customer_details = silver_order_customer_details(spark)
    df_Cleanup = Cleanup(spark, df_silver_order_customer_details)
    df_total_by_zip_and_date = total_by_zip_and_date(spark, Config.total_by_zip_and_date, df_Cleanup)
    df_customer_order_total = customer_order_total(spark, df_silver_order_customer_details)
    gold_sales_by_zip_date(spark, df_total_by_zip_and_date)
    df_order_by_total_amount_desc_nulls_first = order_by_total_amount_desc_nulls_first(spark, df_customer_order_total)
    df_SumAmounts = SumAmounts(spark, df_Cleanup)
    gold_total_sales_by_customer(spark, df_SumAmounts)
    df_limit_10 = limit_10(spark, df_order_by_total_amount_desc_nulls_first)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/gold_sales")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/gold_sales", config = Config)(pipeline)

if __name__ == "__main__":
    main()
