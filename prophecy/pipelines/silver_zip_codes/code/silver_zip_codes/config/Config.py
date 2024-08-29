from silver_zip_codes.graph.irs_zipcode_data_processing.config.Config import (
    SubgraphConfig as irs_zipcode_data_processing_Config
)
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, irs_zipcode_data_processing: dict=None, **kwargs):
        self.spark = None
        self.update(catalog_name, irs_zipcode_data_processing)

    def update(self, catalog_name: str="vlaunir_demos", irs_zipcode_data_processing: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        self.irs_zipcode_data_processing = self.get_config_object(
            prophecy_spark, 
            irs_zipcode_data_processing_Config(prophecy_spark = prophecy_spark), 
            irs_zipcode_data_processing, 
            irs_zipcode_data_processing_Config
        )
        pass
