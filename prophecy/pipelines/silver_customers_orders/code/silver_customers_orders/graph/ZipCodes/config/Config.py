from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, catalog_name: str="vlaunir_demos", **kwargs):
        self.catalog_name = catalog_name
        pass

    def update(self, updated_config):
        self.catalog_name = updated_config.catalog_name
        pass

Config = SubgraphConfig()
