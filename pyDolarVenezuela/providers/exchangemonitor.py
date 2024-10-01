from typing import Any, Dict, List
from datetime import datetime
import requests
import pytz
import aiohttp
import asyncio

from ..network import _headers
from ..utils.common import _convert_specific_format, _parse_price, _parse_percent
from ..utils.time import get_formatted_date

from ._base import Base
from ..pages import ExchangeMonitor as ExchangeMonitorPage


class ExchangeMonitor(Base):
    PAGE = ExchangeMonitorPage

    @classmethod
    async def _load_async(cls, **kwargs) -> List[Dict[str, Any]]:
        tz = pytz.timezone('America/Caracas')
        url = f'{cls.PAGE.provider}/data/data-rates/ve'

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=_headers) as response:
                if response.status == 200:
                    data_json = await response.json()
                    # ... (resto del procesamiento de datos) ...
                    return result
                else:
                    print(f"Error retrieving data from API: {response.status}")
                    return []

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        return asyncio.run(cls._load_async(**kwargs))
