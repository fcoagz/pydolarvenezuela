import json
from .. import network
from ..utils import time
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

class AlCambio:
    def __init__(self, url: str, **kwargs) -> None:
        response = network.curl('POST', url, headers, data)
        self.json_response = json.loads(response)
    
    def _load(self):
        self.rates = []
        country_conversions = self.json_response['data']['getCountryConversions']
        rate_types = ['PRIMARY', 'SECONDARY']

        for rate in country_conversions['conversionRates']:
            if rate['type'] in rate_types:
                key = 'enparalelovzla' if not rate['official'] else 'bcv'
                name = 'EnParaleloVzla' if not rate['official'] else 'BCV'
                date = time.get_formatted_timestamp(country_conversions['dateParalelo'] if not rate['official'] else country_conversions['dateBcv'])
                image = next((image.image for image in list_monitors_images if image.provider == 'alcambio' and image.title == key), None)
                self.rates.append({
                    'key': key,
                    'title': name,
                    'price': rate['baseValue'],
                    'last_update': date,
                    'image': image
                })
                rate_types.remove(rate['type'])

            if not rate_types:
                break

    def get_values(self):
        self._load()
        return self.rates