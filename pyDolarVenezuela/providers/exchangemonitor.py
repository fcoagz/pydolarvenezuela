from typing import Any, Dict, List
from datetime import datetime
import requests
import pytz

from ..network import _headers
from ..utils.common import _convert_specific_format, _parse_price, _parse_percent
from ..utils.time import get_formatted_date

from ._base import Base
from ..pages import ExchangeMonitor as ExchangeMonitorPage


class ExchangeMonitor(Base):
    PAGE = ExchangeMonitorPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        tz = pytz.timezone('America/Caracas')

        url = f'{cls.PAGE.provider}/data/data-rates/ve'

        # Realizar la solicitud GET a la API
        response = requests.get(url, headers=_headers)

        # Verificar que la solicitud fue exitosa
        if response.status_code == 200:
            data_json = response.json()

            # Extraer los datos requeridos
            result = []
            for item in data_json["data"]:
                # Parsear la fecha y hora (sin zona horaria)
                date_naive = datetime.strptime(item.get("date"), "%d-%m-%Y %I:%M %p")

                # Asignar y formatear valores
                date_aware = str(tz.localize(date_naive))
                logo = item.get("logo")
                net_change = _parse_percent(item.get("change_rate"))
                net_chg = str(item.get("change_rate"))
                color = "red" if "-" in net_chg else "green" if "+" in net_chg else ""
                symbol = "▼" if "-" in net_chg else "▲" if "+" in net_chg else "neutral"

                extracted_data = {
                    "key": _convert_specific_format(item.get("id")),
                    "title": _convert_specific_format(item.get("name")),
                    "price": _parse_price(item.get("rate")),
                    "price_old": _parse_price(item.get("last_rate")),
                    "last_update":get_formatted_date(date_aware),
                    "percent": _parse_percent(item.get("change_perc")),
                    "change": net_change,
                    "color": color,
                    "symbol": symbol,
                    "image": f'{cls.PAGE.provider}{logo}'
                }
                result.append(extracted_data)

            return result

        else:
            print(f"Error retrieving data from API: {response.status_code}")
            return []
