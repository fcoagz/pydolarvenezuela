from typing import Any, Dict, List
from bs4 import BeautifulSoup

from ..network import requests, get
from ..utils.extras import currencies, list_monitors_images, bank_dict
from ..utils.time import get_formatted_date_bcv, get_datestring_to_datetime
from ._base import Base
from ..pages import BCV as BCVPage

requests.packages.urllib3.disable_warnings()

def _get_rate_by_id(tag_id: str, soup: BeautifulSoup):
    return float(soup.find(id=tag_id).find('strong').text.strip().replace(',', '.'))

def _get_time(soup: BeautifulSoup):
    date = soup.find('span', 'date-display-single').get('content')
    return get_formatted_date_bcv(date)

class BCV(Base):
    PAGE = BCVPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        response = get(f'{cls.PAGE.provider}tasas-informativas-sistema-bancario', verify=False)
        soup = BeautifulSoup(response, 'html.parser')
        rates = []

        section_tipo_de_cambio_oficial = soup.find('div', 'view-tipo-de-cambio-oficial-del-bcv')
        section_sistema_bancario = soup.find('div', 'table-responsive')

        for bank in section_sistema_bancario.find('tbody').find_all('tr'):
            title = str(bank.find('td', 'views-field views-field-views-conditional').text).strip()
            key = bank_dict.get(title)

            if key and key not in [bank['key'] for bank in rates]:
                field_tasa_venta = bank.find('td', 'views-field views-field-field-tasa-venta').text
                if field_tasa_venta.count(',') == 1:
                    price = float(field_tasa_venta.replace(',', '.'))
                    price_round = round(price, 2)
                    last_update = get_datestring_to_datetime(bank.find('td', 'views-field views-field-field-fecha-del-indicador').text.strip().replace('-', '/'))

                    rates.append({
                        'key': key,
                        'title': title,
                        'price': price_round,
                        'last_update': last_update
                    })

        for code, values in currencies.items():
            image = next((image.image for image in list_monitors_images if image.provider == 'bcv' and image.title == code), None)
            rates.append({
                'key': code,
                'title': values['name'],
                'price': round(_get_rate_by_id(values['id'], section_tipo_de_cambio_oficial), 2),
                'image': image,
                'last_update': _get_time(section_tipo_de_cambio_oficial)
            })

        return rates 