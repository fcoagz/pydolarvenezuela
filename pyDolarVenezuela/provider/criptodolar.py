from pyDolarVenezuela import network
from pyDolarVenezuela.tools import TimeDollar

import json

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _convert_dollar_name_to_monitor_name(monitor_name: str):
    if monitor_name.split(' ')[0] == 'Dólar' and monitor_name != 'Dólar Today':
        if monitor_name == 'Dólar Monitor':
            return 'EnParaleloVzla'
        else:
            return monitor_name.split(' ')[1]
    return monitor_name

class CriptoDolar:
    def __init__(self, url: str) -> None:
        response           = network.get(url + "coins/latest")
        self.json_response = json.loads(response)
    
    def _load(self):
        t = TimeDollar()
        self.data = {}

        for monitor in self.json_response:
            if 'bolivar' in monitor['type'] or 'bancove' in monitor['type']:
                data = {
                    'title': _convert_dollar_name_to_monitor_name(monitor['name']),
                    'price': monitor['price'],
                    'price_old': monitor['priceOld'],
                    'type': 'bank' if monitor['type'] == 'bancove' else 'monitor',
                    'last_update': t.get_time(monitor['updatedAt']),
                }

                self.data[_convert_specific_format(data['title'])] = data
    
    def get_values(self, monitor_code: str = None, name_property: str = None, prettify: bool = True):
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