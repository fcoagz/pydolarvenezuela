from bs4 import BeautifulSoup
from .. import network
from ..tools import time

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _get_values_monitors(soup: BeautifulSoup):
    return [value for value in soup]

class ExchangeMonitor:
    def __init__(self, url: str, currency: str, **kwargs) -> None:
        response = (network.curl(url + "dolar-venezuela") if currency == 'usd'
                    else network.curl(url + "dolar-venezuela/EUR"))
        self.soup = BeautifulSoup(response, "html.parser")
    
    def _load(self):
        section_dolar_venezuela = self.soup.find_all("div", "col-xs-12 col-sm-6 col-md-4 col-tabla")
        _scraping_monitors = _get_values_monitors(section_dolar_venezuela)

        self.data = {}
        for scraping_monitor in _scraping_monitors:
            result = scraping_monitor.find("div", "module-table module-table-fecha")

            name  = result.find("h6", "nombre").text
            price = str(result.find('p', "precio").text).replace(',', '.')

            if price.count('.') == 2:
                price = price.replace('.', '', 1)

            price = float(price)
            last_update = time.get_formatted_time(' '.join(str(result.find('p', "fecha").text).split(' ')[1:]).capitalize())
            symbol = str(result.find('p', "cambio-por").text)[0] if not str(result.find('p', "cambio-por").text)[0] == ' ' else ''
            color  = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
            percent = float(str(result.find('p', "cambio-por").text)[1:].strip().replace(',', '.').replace('%', ''))
            change = float(str(result.find('p', "cambio-num").text).replace(',', '.'))

            data = {
                'title': name,
                'price': price,
                'last_update': last_update,
                'percent': percent,
                'change': change,
                'color': color,
                'symbol': symbol
            }

            self.data[_convert_specific_format(name)] = data
    
    def get_values(self):
        self._load()
        return self.data