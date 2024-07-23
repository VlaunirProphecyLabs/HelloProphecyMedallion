from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, source_path: str="", updated_at: str="", tablename: str="", **kwargs):
        self.source_path = source_path
        self.updated_at = updated_at
        self.tablename = tablename
        pass

    def update(self, updated_config):
        self.source_path = updated_config.source_path
        self.updated_at = updated_config.updated_at
        self.tablename = updated_config.tablename
        pass

Config = SubgraphConfig()
