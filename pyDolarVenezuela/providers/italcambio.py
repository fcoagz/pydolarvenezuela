from typing import Any, Dict, List
from datetime import datetime
from bs4 import BeautifulSoup

from ..network import get
from ..utils.time import standard_time_zone
from ..utils.extras import code_currencies
from ._base import Base
from ..pages import Italcambio as ItalcambioPage

class Italcambio(Base):
    PAGE = ItalcambioPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        response = get(cls.PAGE.provider)
        soup = BeautifulSoup(response, 'html.parser')
        section_currencies_italcambio = soup.find('div', 'container-fluid compra')
        monitors_amounts = [x.text for x in section_currencies_italcambio.find_all('p', 'small')]

        rates = []
        for i in range(len(monitors_amounts)):
            if i%2 == 0:
                title = code_currencies[monitors_amounts[i]]
                key = monitors_amounts[i].lower()
                price_old = float(str(monitors_amounts[i-1]).split()[-1])
                price = round(price_old, 2)
                dt = datetime.now(standard_time_zone)
                dt_tostring = dt.isoformat()

                rates.append({
                    'key': key,
                    'title': title,
                    'price': price,
                    'price_old': price_old,
                    'last_update': dt_tostring
                })

        return rates