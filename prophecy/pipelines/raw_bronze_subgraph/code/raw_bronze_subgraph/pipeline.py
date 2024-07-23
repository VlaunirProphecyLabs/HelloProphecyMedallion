from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *
from prophecy.utils import *
from raw_bronze_subgraph.graph import *

def pipeline(spark: SparkSession) -> None:
    df_create_dataframe_from_urls = create_dataframe_from_urls(spark)
    df_add_load_date = add_load_date(spark, df_create_dataframe_from_urls)
    load_csv_data(Config.load_csv_data).apply(spark, df_add_load_date)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("raw_bronze_subgraph")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/raw_bronze_subgraph")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/raw_bronze_subgraph", config = Config)(pipeline)

if __name__ == "__main__":
    main()
