from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from silver_zip_codes.config.ConfigStore import *
from silver_zip_codes.udfs import *
from prophecy.utils import *
from silver_zip_codes.graph import *

def pipeline(spark: SparkSession) -> None:
    df_irs_zipcode_data_processing = irs_zipcode_data_processing(spark, Config.irs_zipcode_data_processing)
    df_add_sequence_column_1 = add_sequence_column_1(spark, df_irs_zipcode_data_processing)
    silver_irs_zipcode(spark, df_add_sequence_column_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver_zip_codes")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/silver_zip_codes", config = Config)(pipeline)

if __name__ == "__main__":
    main()
