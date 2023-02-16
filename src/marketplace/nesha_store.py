import logging
import requests

import src.utils.handler as handler
class NeshaStore:
    def __init__(self, skin_name) -> None:
        self.url = f"https://api.neshastore.com/items?orderBy%5B%5D=2&tradeLocked=true&limit=150&query={ handler.handle_skin_name_to_url(skin_name).lower() }"
        self.get_raw_data()

    def get_raw_data(self) -> None:
        data = requests.get(self.url)
        if data.status_code != 200:
            logging.error(msg=f'COULD NOT RETRIEVE DATA FROM {__name__}')
        
        self.raw_data = data.json().get('items')

    def handle_raw_data(self) -> list:
        if not self.raw_data:
            logging.error(msg=f'COULD NOT RETRIEVE DATA FROM {__name__}')
            return
        
        return list(map(lambda item:{
            'name': item.get('name'),
            'price': item.get('price'),
            'stickets': item.get('stickers') if len(item.get('stickers')) > 0 else None,
            'float': item.get('float'),
            'inspect_link': item.get('inspectLink'),
            'tradeLock': item.get('tradelockExpiration')
        }, self.raw_data))
        


    def get_skin_name(self, div):
        return div.find_all('img')[-1].get('alt')

    def get_skin_price(self, div):
        return handler.normalize_data(div.find(class_='font-weight-normal h2').text).replace(' ', '')

    def get_trade_lock_time(self, div):
        return div.find_all('span')[0].text
    
    
