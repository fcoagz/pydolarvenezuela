from pyDolarVenezuela import network
from pyDolarVenezuela.tools import TimeDollar

import json

monitors = {'binance': 'Binance', 'dolartoday': 'DolarToday', 'yadio': 'Yadio', 'airtm': 'Airtm', 'cambiosrya': 'Cambios R&A', 'mkambio': 'Mkambio', 'bcv': 'BCV', 'promediovip': 'EnParaleloVzlaVip', 'prom_epv': 'EnParalelovzla'}

class Dpedidos:
    def __init__(self, url: str) -> None:
        response           = network.get(url + 'minmaxhistorial')
        json_response = json.loads(response)

        self.json_response = json_response['result'][0]
    
    def get_values(self, monitor_code: str = None, name_property: str = None, prettify: bool = True):
        t = TimeDollar()
        result = {}

        for key, title in monitors.items():
            if key in self.json_response and self.json_response[key] not in ['0', None]:
                data = {
                    'title': title,
                    'price': round(float(self.json_response[key]), 2)
                }

                if key == 'prom_epv':
                    data['last_update'] = t.get_time(f"{self.json_response['fecha_epv']} {'13' if self.json_response['hora_epv'] == '1' else self.json_response['hora_epv']}:00", True)
                
                result[title.lower()] = data
        result['last_update'] = t.get_time(f"{self.json_response['fecha']} {self.json_response['hora']}", True)

        if not monitor_code:
            return result
        
        try:
            monitor_data = result[monitor_code.lower()]
            if name_property:
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")