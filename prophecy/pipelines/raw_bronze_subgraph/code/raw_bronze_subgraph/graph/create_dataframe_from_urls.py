from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from raw_bronze_subgraph.config.ConfigStore import *
from raw_bronze_subgraph.functions import *

def create_dataframe_from_urls(spark: SparkSession) -> DataFrame:
    schema = StructType([
            StructField("tablename", StringType(), True),
            StructField("source_path", StringType(), True)

    ])
    # Sample data
    data = [("bronze_customers", "s3a://prophecy-dataset-samples/CustomersDataset*.csv"),
            ("bronze_customers", "s3a://prophecy-dataset-samples/Orders*.csv"),
            ("bronze_irs_zipcode", "dbfs:/databricks-datasets/data.gov/irs_zip_code_data/*/")]
    # Create DataFrame
    df = spark.createDataFrame(data, schema = schema)
    # Show DataFrame
    out0 = df

    return out0
