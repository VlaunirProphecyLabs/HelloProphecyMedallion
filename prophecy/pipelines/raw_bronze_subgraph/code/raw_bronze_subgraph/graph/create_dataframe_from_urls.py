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
    # https://www.irs.gov/pub/irs-soi/13zpallagi.csv
    data = [("bronze_customers", "s3://prophecy-dataset-samples/CustomersDataset*.csv"),
            ("bronze_orders", "s3://prophecy-dataset-samples/Orders*.csv"),
            ("bronze_irs_zipcode",
             "dbfs:/databricks-datasets/data.gov/irs_zip_code_data/data-001/2013_soi_zipcode_agi.csv"),
            ("bronze_account_detail", "dbfs:/Users/vlaunir@prophecy.io/delimited/account_detail.csv"),
            ("bronze_item_detail", "dbfs:/Users/vlaunir@prophecy.io/delimited/item_detail.csv")]
    print(Config.catalog_name)
    # Create DataFrame
    df = spark.createDataFrame(data, schema = schema)
    # Show DataFrame
    out0 = df

    return out0
