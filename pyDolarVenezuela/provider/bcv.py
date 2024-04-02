import requests
from bs4 import BeautifulSoup

from ..utils import currencies

requests.packages.urllib3.disable_warnings()

def _get_rate_by_id(tag_id: str, soup: BeautifulSoup):
    return float(soup.find(id=tag_id).find("strong").text.strip().replace(',', '.'))

def _get_time(soup: BeautifulSoup):
    date = soup.find("span", "date-display-single").get('content')
    return date.split('T')[0].replace('-', '/')

class BCV:
    def __init__(self, url: str, currency: str) -> None:
        response      = requests.get(url, verify=False)
        response.raise_for_status()

        self.soup     = BeautifulSoup(response.content, 'html.parser')
        self.currency = currency

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

    def get_values(self, **kwargs):
        currency_code = kwargs.get('monitor_code')
        name_property = kwargs.get('name_property')
        prettify = kwargs.get('prettify', False)
        
        self._load()

        if not currency_code:
            return self.rates
        
        try:
            monitor_data = self.rates[currency_code.lower()]
            if name_property:
                if name_property == 'last_update':
                    return self.rates['last_update']
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")