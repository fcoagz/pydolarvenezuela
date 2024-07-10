from typing import Any, Dict, List
import json

from .. import network
from ..utils import time
from ..utils.extras import list_monitors_images
from ._base import Base
from ..pages import CriptoDolar as CriptoDolarPage

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _convert_dollar_name_to_monitor_name(monitor_name: str):
    if monitor_name.split(' ')[0] in ['Dólar', 'Euro'] and monitor_name not in ['Dólar Today', 'Euro Today']:
        if monitor_name in ['Dólar Monitor', 'Euro Monitor']:
            return 'EnParaleloVzla'
        else:
            return monitor_name.split(' ')[1]
    return monitor_name

class CriptoDolar(Base):
    PAGE = CriptoDolarPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        response = network.get(f'{cls.PAGE.provider}coins/latest', {'type': 'bolivar', 'base': kwargs.get('currency', 'usd')})
        json_response = json.loads(response)
        data = []

        for monitor in json_response:
            if monitor['type'] in ['bolivar', 'bancove']:
                image = next((image.image for image in list_monitors_images if image.provider == 'criptodolar' and image.title == _convert_specific_format(
                        _convert_dollar_name_to_monitor_name(monitor['name']))), None)
                key = _convert_specific_format(_convert_dollar_name_to_monitor_name(monitor['name']))
                title = _convert_dollar_name_to_monitor_name(monitor['name'])
                price = round(monitor['price'], 2)
                price_old   = monitor['priceOld']
                last_update = time.get_time_standard(monitor['updatedAt'])

                data.append({
                    'key': key,
                    'title': title,
                    'price': price,
                    'price_old': price_old,
                    'last_update': last_update,
                    'image': image
                })

        return data