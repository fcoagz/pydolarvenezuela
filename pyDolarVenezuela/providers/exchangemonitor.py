from typing import Any, Dict, List, Union
from bs4 import BeautifulSoup

from .. import network
from ..utils import time
from ..utils.extras import list_monitors_images
from ._base import Base
from ..pages import ExchangeMonitor as ExchangeMonitorPage

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _get_values_monitors(soup: BeautifulSoup):
    return [value for value in soup]

class ExchangeMonitor(Base):
    PAGE = ExchangeMonitorPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        try:
            url = f'{cls.PAGE.provider}dolar-venezuela' if not kwargs.get('currency') == 'usd' else f'{cls.PAGE.provider}dolar-venezuela/EUR'
            response = network.curl('GET', url)
            soup = BeautifulSoup(response, 'html.parser')
            
            section_dolar_venezuela = soup.find_all("div", "col-xs-12 col-sm-6 col-md-4 col-tabla")
            _scraping_monitors = _get_values_monitors(section_dolar_venezuela)
            data = []

            for scraping_monitor in _scraping_monitors:
                result = scraping_monitor.find("div", "module-table module-table-fecha")

                name  = result.find("h6", "nombre").text
                key = _convert_specific_format(name)
                price = str(result.find('p', "precio").text).replace(',', '.')

                if price.count('.') == 2:
                    price = price.replace('.', '', 1)

                price = float(price)
                last_update = time.get_formatted_time(' '.join(str(result.find('p', "fecha").text).split(' ')[1:]).capitalize())
                symbol = str(result.find('p', "cambio-por").text)[0] if not str(result.find('p', "cambio-por").text)[0] == ' ' else ''
                color  = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
                percent = float(str(result.find('p', "cambio-por").text)[1:].strip().replace(',', '.').replace('%', ''))
                change = float(str(result.find('p', "cambio-num").text).replace(',', '.'))
                image = next((image.image for image in list_monitors_images if image.provider == 'exchangemonitor' and image.title == _convert_specific_format(name)), None)

                data.append({
                    'key': key,
                    'title': name,
                    'price': price,
                    'last_update': last_update,
                    'percent': percent,
                    'change': change,
                    'color': color,
                    'symbol': symbol,
                    'image': image
                })

            return data
        except Exception as e:
            raise Exception(f"Error al cargar los datos del ExchangeMonitor: {e}")