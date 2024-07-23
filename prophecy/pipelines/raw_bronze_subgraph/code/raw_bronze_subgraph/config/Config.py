from raw_bronze_subgraph.graph.load_csv_data.config.Config import SubgraphConfig as load_csv_data_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, load_csv_data: dict=None, catalog_name: str=None, **kwargs):
        self.spark = None
        self.update(load_csv_data, catalog_name)

    def update(self, load_csv_data: dict={}, catalog_name: str="vlaunir_demos", **kwargs):
        prophecy_spark = self.spark
        self.load_csv_data = self.get_config_object(
            prophecy_spark, 
            load_csv_data_Config(prophecy_spark = prophecy_spark), 
            load_csv_data, 
            load_csv_data_Config
        )
        self.catalog_name = catalog_name
        pass
