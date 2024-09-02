from typing import Any, Dict, List
from datetime import datetime
import json

from .. import network
from ..utils.extras import list_monitors_images
from ..utils.common import _convert_specific_format, _convert_dollar_name_to_monitor_name
from ..utils.time import standard_time_zone
from ._base import Base
from ..pages import DolarToday as DolarTodayPage


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
