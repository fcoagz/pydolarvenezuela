import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def _get_rate_by_id(tag_id: str, soup: BeautifulSoup):
    return soup.find(id=tag_id).find("strong").text.strip().replace(',', '.')

def _get_time(soup: BeautifulSoup):
    date = soup.find("span", "date-display-single")
    return [date.text.strip().replace('  ', ' '), date.get("content").split('T')[0]]

class BCV:
    def __init__(self, url: str) -> None:
        response  = requests.get(url, verify=False)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")
    
    def _load(self) -> None:
        section_tipo_de_cambio_oficial = self.soup.find("div", "view-tipo-de-cambio-oficial-del-bcv")

        self.rates = {
            "eur": {"currency": "Euro", "price": _get_rate_by_id("euro", section_tipo_de_cambio_oficial)},
            "cny": {"currency": "Yuan chino", "price": _get_rate_by_id("yuan", section_tipo_de_cambio_oficial)},
            "try": {"currency": "Lira turca", "price": _get_rate_by_id("lira", section_tipo_de_cambio_oficial)},
            "rub": {"currency": "Rublo ruso", "price": _get_rate_by_id("rublo", section_tipo_de_cambio_oficial)},
            "usd": {"currency": "Dólar estadounidense", "price": _get_rate_by_id("dolar", section_tipo_de_cambio_oficial)},
            "date": _get_time(section_tipo_de_cambio_oficial)
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