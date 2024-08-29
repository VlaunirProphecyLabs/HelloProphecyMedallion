from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, catalog_name: str=None, **kwargs):
        self.spark = None
        self.update(catalog_name)

    def update(self, catalog_name: str="vlaunir_demos", **kwargs):
        prophecy_spark = self.spark
        self.catalog_name = catalog_name
        pass
