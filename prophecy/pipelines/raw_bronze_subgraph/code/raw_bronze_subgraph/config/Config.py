from raw_bronze_subgraph.graph.raw_data_pipeline.config.Config import SubgraphConfig as raw_data_pipeline_Config
from raw_bronze_subgraph.graph.irs_zipcodes_data.config.Config import SubgraphConfig as irs_zipcodes_data_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            raw_data_pipeline: dict=None,
            catalog_name: str=None,
            source_files_path: str=None,
            irs_zipcodes_data: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(raw_data_pipeline, catalog_name, source_files_path, irs_zipcodes_data)

    def update(
            self,
            raw_data_pipeline: dict={},
            catalog_name: str="vlaunir_demos",
            source_files_path: str="dbfs:/Users/vlaunir@prophecy.io/source_files.csv",
            irs_zipcodes_data: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.raw_data_pipeline = self.get_config_object(
            prophecy_spark, 
            raw_data_pipeline_Config(prophecy_spark = prophecy_spark), 
            raw_data_pipeline, 
            raw_data_pipeline_Config
        )
        self.catalog_name = catalog_name
        self.source_files_path = source_files_path
        self.irs_zipcodes_data = self.get_config_object(
            prophecy_spark, 
            irs_zipcodes_data_Config(prophecy_spark = prophecy_spark), 
            irs_zipcodes_data, 
            irs_zipcodes_data_Config
        )
        pass
