from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *
from prophecy.utils import *
from gold_sales.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_order_customer_details = silver_order_customer_details(spark)
    df_deduplicate_customers = deduplicate_customers(spark, df_silver_order_customer_details)
    df_category_count_by_order = category_count_by_order(spark, df_silver_order_customer_details)
    df_category_count_desc = category_count_desc(spark, df_category_count_by_order)
    df_top_10_records = top_10_records(spark, df_category_count_desc)
    df_Filter_1 = Filter_1(spark, df_top_10_records)
    df_Cleanup = Cleanup(spark, df_silver_order_customer_details)
    df_total_by_zip_and_date = total_by_zip_and_date(spark, Config.total_by_zip_and_date, df_Cleanup)
    gold_sales_by_zip_date(spark, df_total_by_zip_and_date)
    df_SumAmounts = SumAmounts(spark, df_Cleanup)
    gold_total_sales_by_customer(spark, df_SumAmounts)

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
