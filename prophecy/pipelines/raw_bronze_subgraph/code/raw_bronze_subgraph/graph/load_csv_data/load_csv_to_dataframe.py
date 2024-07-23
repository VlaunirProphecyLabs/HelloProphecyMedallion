from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from raw_bronze_subgraph.functions import *

def load_csv_to_dataframe(spark: SparkSession) -> DataFrame:
    # Import pandas library
    import pandas as pd
    # URL or path to your CSV file
    csv_file_path = Config.source_path
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    out0 = spark.createDataFrame(df)

    return out0
