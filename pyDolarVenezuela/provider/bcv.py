from pyDolarVenezuela.utils import currencies

import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def _get_rate_by_id(tag_id: str, soup: BeautifulSoup):
    return float(soup.find(id=tag_id).find("strong").text.strip().replace(',', '.'))

def _get_time(soup: BeautifulSoup):
    date = soup.find("span", "date-display-single")
    return date.text.strip().replace('  ', ' ')

class BCV:
    def __init__(self, url: str) -> None:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        self.soup = BeautifulSoup(response.content, 'html.parser')

    def _load(self) -> None:
        section_tipo_de_cambio_oficial = self.soup.find("div", "view-tipo-de-cambio-oficial-del-bcv")

        self.rates = {}
        self.rates['last_update'] = _get_time(section_tipo_de_cambio_oficial)

        for code, values in currencies.items():
            self.rates[code] = {
                "title": values['name'],
                "price": round(_get_rate_by_id(values['id'], section_tipo_de_cambio_oficial), 2),
                "price_old": _get_rate_by_id(values['id'], section_tipo_de_cambio_oficial)
            }

    def get_values(self, currency_code: str = None, name_property: str = None, prettify: bool = True):
        self._load()

        if not currency_code:
            return self.rates
        
        try:
            monitor_data = self.rates[currency_code.lower()]
            if name_property:
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")