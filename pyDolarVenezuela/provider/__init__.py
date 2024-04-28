import json
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor

from ..data.redis import Cache
from ..models.database import Redis
from ..models.pages import Page
from ..pages import BCV as B, CriptoDolar as C, ExchangeMonitor as E

monitor_classes = [
    {
        B.name: {
            'currency': ['usd', 'eur'],
            'provider': BCV
        }
    },
    {
        C.name: {
            'currency': ['usd', 'eur'],
            'provider': CriptoDolar
        }
    },
    {
        E.name: {
            'currency': ['usd', 'eur'],
            'provider': ExchangeMonitor
        }
    }
]

def select_monitor(provider: Page, db: Redis, **kwargs):
    global data
        
    currency = kwargs.get('currency')
    monitor_code = kwargs.get('monitor_code')
    name_property = kwargs.get('name_property')
    prettify = kwargs.get('prettify', False)

    if currency not in ['usd', 'eur']:
            raise ValueError(f"The currency type must be 'usd' or 'eur', not {currency}")

    def _get_values_specifics():
        if not monitor_code:
            return data
        
        try:
            monitor_data = data[monitor_code.lower()]
            if name_property:
                if name_property == 'last_update' and provider.name == B.name:
                    return data[name_property]
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")

    try:
        monitor_class = None

        for monitor in monitor_classes:
            if monitor.get(provider.name) and currency in monitor.get(provider.name)['currency']:
                monitor_class = monitor[provider.name]['provider']

        if monitor_class is not None:
            data = monitor_class(provider.provider, currency).get_values()
            if db is not None:
                key = f'{currency}:{provider.name}'
                cache = Cache(db)

                existing_data = cache.get_data(key)

                if not existing_data:
                    cache.set_data(key, json.dumps(data), db.ttl)
                else:
                    existing_data_dict: dict[str, dict] = json.loads(existing_data)
                    for name in existing_data_dict:
                        if not name == 'last_update':
                            if name in existing_data_dict and name in data:
                                if existing_data_dict[name]['price'] != data[name]['price']:
                                    price = existing_data_dict[name]['price']
                                    new_price = data[name]['price']
                                    change  = round(float(new_price - price), 2)
                                    percent = float(f'{round(float((change / new_price) * 100 if price != 0 else 0), 2)}'.replace('-', ' '))
                                    symbol  = "" if change == 0 else "▲" if change >= 0 else "▼"
                                    color   = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
                                    last_update = None if provider.name == B.name else data[name]['last_update']
                                    change = float(str(change).replace('-', ' '))

                                    if not provider.name == B.name:
                                        existing_data_dict[name].update({
                                            'price': new_price,
                                            'change': change,
                                            'percent': percent,
                                            'color': color,
                                            'symbol': symbol,
                                            'last_update': last_update
                                        })
                                    else:
                                        existing_data_dict[name].update({
                                            'price': new_price,
                                            'change': change,
                                            'percent': percent,
                                            'color': color,
                                            'symbol': symbol,
                                        })
                        else:
                            existing_data_dict[name] = data[name]
                            
                cache.set_data(key, json.dumps(existing_data_dict), db.ttl)
                data = json.loads(
                    cache.get_data(key)
                )

                return _get_values_specifics()
            
            return _get_values_specifics()
        else:
            raise ValueError("Provider not supported")
    except Exception as e:
        raise e