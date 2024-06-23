import json
from .. import network
from ..utils import time
from ..utils.extras import list_monitors_images

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _convert_dollar_name_to_monitor_name(monitor_name: str):
    if monitor_name.split(' ')[0] in ['Dólar', 'Euro'] and monitor_name not in ['Dólar Today', 'Euro Today']:
        if monitor_name in ['Dólar Monitor', 'Euro Monitor']:
            return 'EnParaleloVzla'
        else:
            return monitor_name.split(' ')[1]
    return monitor_name

class CriptoDolar:
    def __init__(self, url: str, currency: str, **kwargs) -> None:
        response           = (network.get(url + "coins/latest", {'type': 'bolivar', 'base': 'usd'}) if currency == 'usd'
                              else network.get(url + "coins/latest", {'type': 'bolivar', 'base': 'eur'}))
        self.json_response = json.loads(response)
        self.currency = currency
    
    def _load(self):
        self.data = []

        for monitor in self.json_response:
            if monitor['type'] in ['bolivar', 'bancove']:
                image = next((image.image for image in list_monitors_images if image.provider == 'criptodolar' and image.title == _convert_specific_format(
                    _convert_dollar_name_to_monitor_name(monitor['name']))), None)
                key = _convert_specific_format(_convert_dollar_name_to_monitor_name(monitor['name']))
                data = {
                    'key': key,
                    'title': _convert_dollar_name_to_monitor_name(monitor['name']),
                    'price': round(monitor['price'], 2),
                    'price_old': monitor['priceOld'],
                    'last_update': time.get_time_standard(monitor['updatedAt']),
                    'image': image
                }

                self.data.append(data)
    
    def get_values(self):
        self._load()
        return self.data
