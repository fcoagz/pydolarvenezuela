import json
from typing import Any, Dict, List

from .. import network
from ..utils import time
from ._base import Base
from ..pages import AlCambio as AlCambioPage
from ..utils.extras import list_monitors_images

headers = {
    "accept": "*/*",
    "accept-language": "es-ES,es;q=0.7",
    "apollographql-client-name": "web",
    "apollographql-client-version": "1.0.0",
    "content-type": "application/json",
}

data = {
    "operationName": "getCountryConversions",
    "variables": {
        "countryCode": "VE"
    },
    "query": """
    query getCountryConversions($countryCode: String!) {
      getCountryConversions(payload: {countryCode: $countryCode}) {
        _id
        baseCurrency {
          code
          decimalDigits
          name
          rounding
          symbol
          symbolNative
          __typename
        }
        country {
          code
          dial_code
          flag
          name
          __typename
        }
        conversionRates {
          baseValue
          official
          principal
          rateCurrency {
            code
            decimalDigits
            name
            rounding
            symbol
            symbolNative
            __typename
          }
          rateValue
          type
          __typename
        }
        dateBcvFees
        dateParalelo
        dateBcv
        createdAt
        __typename
      }
    }
    """
}

class AlCambio(Base):
    PAGE = AlCambioPage

    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        response = network.curl('POST', cls.PAGE.provider, headers, data)
        json_response = json.loads(response)

        rates = []
        country_conversions = json_response['data']['getCountryConversions']
        rate_types = ['PRIMARY', 'SECONDARY']

        for rate in country_conversions['conversionRates']:
            if rate['type'] in rate_types:
                key = 'enparalelovzla' if not rate['official'] else 'bcv'
                name = 'EnParaleloVzla' if not rate['official'] else 'BCV'
                date = time.get_formatted_timestamp(country_conversions['dateParalelo'] if not rate['official'] else country_conversions['dateBcv'])
                image = next((image.image for image in list_monitors_images if image.provider == 'alcambio' and image.title == key), None)
                rates.append({
                    'key': key,
                    'title': name,
                    'price': rate['baseValue'],
                    'last_update': date,
                    'image': image
                })
                rate_types.remove(rate['type'])

            if not rate_types:
                    break
            
        return rates