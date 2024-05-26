from datetime import datetime
from bs4 import BeautifulSoup
from ..network import get
from ..utils.time import standard_time_zone
from ..utils.extras import code_currencies

class Italcambio:
    def __init__(self, url: str, **kwargs) -> None:
        response = get(url)
        self.soup = BeautifulSoup(response, 'html.parser')

    def _load(self):
        section_currencies_italcambio = self.soup.find('div', 'container-fluid compra')
        monitors_amounts = [x.text for x in section_currencies_italcambio.find_all('p', 'small')]

        self.rates = {}
        for i in range(len(monitors_amounts)):
            if i%2 == 0:
                title = code_currencies[monitors_amounts[i]]
                price_old = float(str(monitors_amounts[i-1]).split()[-1])
                price = round(price_old, 2)
                dt = datetime.now(standard_time_zone)
                dt_tostring = dt.strftime('%d/%m/%Y, %I:%M %p')
    
                self.rates[monitors_amounts[i].lower()] = {
                    'title': title,
                    'price': price,
                    'price_old': price_old,
                    'last_update': dt_tostring
                }
    
    def get_values(self):
        self._load()
        return self.rates