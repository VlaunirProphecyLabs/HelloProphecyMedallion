from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *

def raw_dynamic_source(spark: SparkSession) -> DataFrame:
    df1 = spark.range(1)

    return df1.select(
        lit(
            "[{\"bronze_customers\": \"s3://prophecy-dataset-samples/CustomersDataset*.csv\",\"bronze_orders\": \"s3://prophecy-dataset-samples/Orders*.csv\",\"bronze_irs_zipcode\": \"dbfs:/databricks-datasets/data.gov/irs_zip_code_data/data-001/2013_soi_zipcode_agi.csv\"}]"
          )\
          .alias("sources_input")
    )
