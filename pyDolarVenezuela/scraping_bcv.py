import requests
from bs4 import BeautifulSoup

from request import _get_response_content

requests.packages.urllib3.disable_warnings()

class Bcv:
    def __init__(self) -> None:
        self.page_bcv = "https://www.bcv.org.ve/"
    
    def _get_content(self, web_site: str) -> bytes:
        return _get_response_content(requests.get(web_site))
    
    def _get_value_by_id(self, tag_id: str, soup: BeautifulSoup):
        return soup.find(id=tag_id).find("strong").text.strip().replace(',', '.')
    
    def get_rates(self, currency_code: str):
        content = self._get_content(self.page_bcv)
        soup = BeautifulSoup(content, "html.parser")
        section_tipo_de_cambio_oficial = soup.find("div", "view-tipo-de-cambio-oficial-del-bcv")

        rates = {
            "EUR": self._get_value_by_id("euro", section_tipo_de_cambio_oficial),
            "CNY": self._get_value_by_id("yuan", section_tipo_de_cambio_oficial),
            "TRY": self._get_value_by_id("lira", section_tipo_de_cambio_oficial),
            "RUB": self._get_value_by_id("rublo", section_tipo_de_cambio_oficial),
            "USD": self._get_value_by_id("dolar", section_tipo_de_cambio_oficial)
        }

        if not currency_code:
            return rates
        if currency_code not in rates:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://gothub.com/fcoagz/pydolarvenezuela")
        return rates[currency_code]