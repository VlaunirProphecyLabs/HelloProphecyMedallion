from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from raw_bronze_subgraph.functions import *
from . import *
from .config import *


class load_csv_data(MetaGemExec):

    def __init__(self, config):
        self.config = config
        super().__init__()

    def execute(self, spark: SparkSession, subgraph_config: SubgraphConfig) -> List[DataFrame]:
        Config.update(subgraph_config)
        df_load_csv_to_dataframe = load_csv_to_dataframe(spark)
        df_add_updated_at_column = add_updated_at_column(spark, df_load_csv_to_dataframe)
        raw_table(spark, df_add_updated_at_column)
        subgraph_config.update(Config)

    def apply(self, spark: SparkSession, in0: DataFrame, ) -> None:
        inDFs = []
        conf_to_column = dict(
            [("source_path", "source_path"), ("updated_at", "updated_at"), ("tablename", "tablename")]
        )

        if in0.count() > 1000:
            raise Exception(f"Config DataFrame row count::{in0.count()} exceeds max run count")

        import multiprocessing
        from multiprocessing.pool import ThreadPool
        from functools import partial

        with ThreadPool(processes = 5) as pool:

            def process_row(row, config, inDFs, spark):
                df1 = config.update_from_row_map(row, conf_to_column)

                return self.__run__(spark, df1, *inDFs)

            partial_process_row = partial(process_row, config = self.config, inDFs = [], spark = spark)
            results = pool.map(partial_process_row, in0.collect())

            return do_union(results)
