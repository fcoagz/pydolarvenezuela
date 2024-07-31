from typing import Any, Dict, List
from datetime import datetime
import json

from .. import network
from ..utils.extras import list_monitors_images
from ..utils.time import standard_time_zone
from ._base import Base
from ..pages import DolarToday as DolarTodayPage

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _convert_dollar_name_to_monitor_name(monitor_name: str):
    if monitor_name.split(' ')[0] in ['Dólar', 'Euro']:
        if monitor_name == 'Dólar Paralelo':
            return 'DolarToday'
        else:
            return monitor_name.split(' ')[1]
    return monitor_name

class DolarToday(Base):
    PAGE = DolarTodayPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        response = network.curl('POST', f'{cls.PAGE.provider}wp-admin/admin-ajax.php', data={
            'action': 'dt_currency_calculator_handler',
            'amount': '1'})
        json_response = json.loads(response)
        data = []

        for key, value in json_response.items():
            title = _convert_dollar_name_to_monitor_name(key)
            key = _convert_specific_format(title)
            image = next((image.image for image in list_monitors_images if image.provider == 'dolartoday' and image.title == key), None)
            price = float(str(value).replace('Bs.', '').strip())   
            last_update = datetime.now(standard_time_zone)

            data.append({
                'key': key,
                'title': title,
                'price': price,
                'last_update': last_update,
                'image': image
            })

        return data
