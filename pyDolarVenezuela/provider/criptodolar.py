import json
from .. import network
from ..tools import time

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
    def __init__(self, url: str, currency: str) -> None:
        response           = (network.get(url + "coins/latest", {'type': 'bolivar', 'base': 'usd'}) if currency == 'usd'
                              else network.get(url + "coins/latest", {'type': 'bolivar', 'base': 'eur'}))
        self.json_response = json.loads(response)
        self.currency = currency
    
    def _load(self):
        self.data = {}

        for monitor in self.json_response:
            if monitor['type'] in ['bolivar', 'bancove']:
                data = {
                    'title': _convert_dollar_name_to_monitor_name(monitor['name']),
                    'price': round(monitor['price'], 2),
                    'price_old': monitor['priceOld'],
                    'type': 'bank' if monitor['type'] == 'bancove' else 'monitor',
                    'last_update': time.get_time_standard(monitor['updatedAt']),
                }

                self.data[_convert_specific_format(data['title'])] = data
    
    def get_values(self, **kwargs):
        monitor_code = kwargs.get('monitor_code')
        name_property = kwargs.get('name_property')
        prettify = kwargs.get('prettify', False)
        
        self._load()

        if not monitor_code:
            return self.data
        
        try:
            monitor_data = self.data[monitor_code.lower()]
            if name_property:
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")