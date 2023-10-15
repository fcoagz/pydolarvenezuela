from pyDolarVenezuela import network
from pyDolarVenezuela.utils import monitors_exchange

import json

class ExchangeMonitor:
    def __init__(self, url: str) -> None:
        self.url = url + "ajax/widget-unique"
    
    def get_values(self, monitor_code: str = None, name_property: str = None, prettify: bool = True):
        results = []

        for monitor in monitors_exchange:
            if not monitor_code or monitor.lower() == monitor_code.lower():
                params   = {'country': 've', 'type': monitor.replace('_', '-')}
                response = network.get(self.url, params=params)
                json_response = json.loads(response)

                data = {
                    'title': json_response['name'],
                    'price': str(json_response['price']).replace(',', '.'),
                    'symbol': json_response['symbol'],
                    'change': json_response['change'],
                    'percent': json_response['percent']
                }

                if name_property:
                    value = data.get(name_property)
                    return f'Bs. {value}' if prettify and name_property == 'price' else value

                results.append(data)

        return results if len(results) > 1 else results[0]