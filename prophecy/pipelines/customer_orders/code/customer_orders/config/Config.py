from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, taxi_data_type: str=None, **kwargs):
        self.spark = None
        self.update(catalog_name, taxi_data_type)

    def update(self, catalog_name: str="vlaunir_demos", taxi_data_type: str="green", **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        self.taxi_data_type = taxi_data_type
        pass
