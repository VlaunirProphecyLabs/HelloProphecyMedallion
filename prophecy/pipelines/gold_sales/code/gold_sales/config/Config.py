from gold_sales.graph.total_by_zip_and_date.config.Config import SubgraphConfig as total_by_zip_and_date_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, total_by_zip_and_date: dict=None, **kwargs):
        self.spark = None
        self.update(catalog_name, total_by_zip_and_date)

    def update(self, catalog_name: str="vlaunir_demos", total_by_zip_and_date: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        self.total_by_zip_and_date = self.get_config_object(
            prophecy_spark, 
            total_by_zip_and_date_Config(prophecy_spark = prophecy_spark), 
            total_by_zip_and_date, 
            total_by_zip_and_date_Config
        )
        pass
