from silver_customers.graph.irs_zipcodes_data.config.Config import SubgraphConfig as irs_zipcodes_data_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, irs_zipcodes_data: dict=None, **kwargs):
        self.spark = None
        self.update(catalog_name, irs_zipcodes_data)

    def update(self, catalog_name: str="vlaunir_demos", irs_zipcodes_data: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        self.irs_zipcodes_data = self.get_config_object(
            prophecy_spark, 
            irs_zipcodes_data_Config(prophecy_spark = prophecy_spark), 
            irs_zipcodes_data, 
            irs_zipcodes_data_Config
        )
        pass
