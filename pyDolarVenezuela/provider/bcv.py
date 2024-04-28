from bs4 import BeautifulSoup

from ..network import requests, get
from ..utils import currencies

requests.packages.urllib3.disable_warnings()

def _get_rate_by_id(tag_id: str, soup: BeautifulSoup):
    return float(soup.find(id=tag_id).find("strong").text.strip().replace(',', '.'))

def _get_time(soup: BeautifulSoup):
    date = soup.find("span", "date-display-single").get('content')
    return date.split('T')[0].replace('-', '/')

class BCV:
    def __init__(self, url: str, *args) -> None:
        response      = get(url, verify=False)
        self.soup     = BeautifulSoup(response, 'html.parser')

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

    def get_values(self):
        self._load()
        return self.rates