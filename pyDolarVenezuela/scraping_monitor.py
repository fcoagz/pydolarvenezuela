import requests
from bs4 import BeautifulSoup

from request import _get_response_content

class Monitor:
    def __init__(self) -> None:
        self.website = 'https://monitordolarvenezuela.com/'

    def _get_content(self, url: str):
        return _get_response_content(requests.get(url))
    
    def _get_results_price(self, soup: BeautifulSoup):
        return [str(x.find('p').text).split(' ')[-1].replace(',', '.') for x in soup.find_all('div', 'col-12 col-sm-4 col-md-2 col-lg-2')]
    
    def get_value_monitors(self, monitor_code: str = None, prettify: bool = False):
        page = self._get_content(self.website)
        soup = BeautifulSoup(page, features='html.parser')

        results = {
            'enparalelovzla': self._get_results_price(soup)[1],
            'monitordolarweb': self._get_results_price(soup)[3],
            'enparalelovzlavip': self._get_results_price(soup)[4],
            'binance': self._get_results_price(soup)[5]
        }

        if not monitor_code:
            return results
        if monitor_code not in results:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://gothub.com/fcoagz/pydolarvenezuela")
        return results[monitor_code] if not prettify else f'Bs. {results[monitor_code]}'