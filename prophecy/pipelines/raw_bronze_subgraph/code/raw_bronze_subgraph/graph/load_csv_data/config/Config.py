from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            source_path: str="",
            updated_at: str="",
            tablename: str="",
            catalog_name: str="vlaunir_demos",
            **kwargs
    ):
        self.source_path = source_path
        self.updated_at = updated_at
        self.tablename = tablename
        self.catalog_name = catalog_name
        pass

    def update(self, updated_config):
        self.source_path = updated_config.source_path
        self.updated_at = updated_config.updated_at
        self.tablename = updated_config.tablename
        self.catalog_name = updated_config.catalog_name
        pass

Config = SubgraphConfig()
