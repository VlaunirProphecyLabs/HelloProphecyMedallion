from silver_customers_orders.graph.bronze_customers.config.Config import SubgraphConfig as bronze_customers_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, bronze_customers: dict=None, **kwargs):
        self.spark = None
        self.update(catalog_name, bronze_customers)

    def update(self, catalog_name: str="vlaunir_demos", bronze_customers: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        self.bronze_customers = self.get_config_object(
            prophecy_spark, 
            bronze_customers_Config(prophecy_spark = prophecy_spark), 
            bronze_customers, 
            bronze_customers_Config
        )
        pass
