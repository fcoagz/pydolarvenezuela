from pyDolarVenezuela import network
from pyDolarVenezuela.tools import time
from pyDolarVenezuela.utils import monitors

import json

class Dpedidos:
    def __init__(self, url: str, currency: str) -> None:
        response           = network.get(url + 'minmaxhistorial')
        json_response      = json.loads(response)

        self.json_response = json_response['result'][0]
        self.currency      = currency
    
    def get_values(self, monitor_code: str, name_property: str, prettify: bool):
        result = {}

        for key, title in monitors.items():
            if key in self.json_response and self.json_response[key] not in ['0', None]:
                data = {
                    'title': title,
                    'price': round(float(self.json_response[key]), 2)
                }

                if key == 'prom_epv':
                    data['last_update'] = time.get_time(f"{self.json_response['fecha_epv']} {'13' if self.json_response['hora_epv'] == '1' else self.json_response['hora_epv']}:00")
                
                result[title.lower()] = data
        result['last_update'] = time.get_time(f"{self.json_response['fecha']} {self.json_response['hora']}")

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