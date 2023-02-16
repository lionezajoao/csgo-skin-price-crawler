import src.utils.config as config
config.logging

from src.marketplace.nesha_store import NeshaStore

class Crawler(NeshaStore):
    def __init__(self, skin_name) -> None:
        super().__init__(skin_name)

    def get_skin_data(self) -> list:
        return self.handle_raw_data()
