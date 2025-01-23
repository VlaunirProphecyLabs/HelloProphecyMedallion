from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *
from prophecy.utils import *
from raw_bronze_subgraph.graph import *

def pipeline(spark: SparkSession) -> None:
    df_gen_source_files = gen_source_files(spark)
    df_add_load_date = add_load_date(spark, df_gen_source_files)
    raw_data_pipeline(Config.raw_data_pipeline).apply(spark, df_add_load_date)
    df_create_dataframe_from_urls = create_dataframe_from_urls(spark)
    df_irs_zipcodes_data = irs_zipcodes_data(spark, Config.irs_zipcodes_data)

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
