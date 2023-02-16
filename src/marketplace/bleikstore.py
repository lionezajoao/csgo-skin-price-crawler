import logging
import requests

from src.utils import handler

class BleikStore:
    def __init__(self, skin_name) -> None:
        self.url = f"https://api.bleikstore.com/api/v1/products?search={ handler.normalize_data(skin_name) }&orderBy=price&orderOperator=DESC"
        pass