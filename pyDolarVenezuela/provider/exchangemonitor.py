from pyDolarVenezuela import network

import json

monitors = ["dolar-em", "monitor_dolar_venezuela", "enparalelovzla", "monitor_dolar_vzla", "petro",
"bcv", "remesas_zoom", "italcambio","bancamiga","banco_de_venezuela","banco-exterior",
"banplus","bnc","banesco","bbva_provincial","mercantil","otras_instituciones",
"binance","airtm","reserve","syklo","yadio",
"dolartoday","mkambio" ,"cambios-r&a" ,"paypal" ,"zinli" ,
"skrill" ,"amazon_gift_card"]

class ExchangeMonitor:
    def __init__(self, url: str) -> None:
        self.url = url + "ajax/widget-unique"
    
    def get_values(self, monitor_code: str = None, name_property: str = None, prettify: bool = True):
        results = []

        for monitor in monitors:
            if not monitor_code or monitor.lower() == monitor_code.lower():
                params   = {'country': 've', 'type': monitor.replace('_', '-')}
                response = network.get(self.url, params=params)
                json_response = json.loads(response)

                data = {
                    'title': json_response['name'],
                    'price': json_response['price'],
                    'symbol': json_response['symbol'],
                    'change': json_response['change'],
                    'percent': json_response['percent']
                }

                if name_property:
                    value = data.get(name_property)
                    return f'Bs. {value}' if prettify and name_property == 'price' else value

                results.append(data)

        return results if len(results) > 1 else results[0]