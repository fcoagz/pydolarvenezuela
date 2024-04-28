import json
from typing import Any
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .italcambio import Italcambio

from ..data.redis import Cache
from ..models.database import Redis
from ..models.pages import Page
from ..pages import BCV as B, CriptoDolar as C, ExchangeMonitor as E, Italcambio as I
from ..utils import currencies_list

monitor_classes = [
    {
        B.name: {
            'currency': B.currencies,
            'provider': BCV
        }
    },
    {
        C.name: {
            'currency': C.currencies,
            'provider': CriptoDolar
        }
    },
    {
        E.name: {
            'currency': E.currencies,
            'provider': ExchangeMonitor
        }
    },
    {
        I.name: {
            'currency': I.currencies,
            'provider': Italcambio
        }
    }
]

def select_monitor(provider: Page, db: Redis, **kwargs):
    global data
        
    currency = kwargs.get('currency')
    monitor_code = kwargs.get('monitor_code')
    name_property = kwargs.get('name_property')
    prettify = kwargs.get('prettify', False)

    if currency not in currencies_list:
        raise ValueError(f"The currency type must be 'usd', 'eur'..., not {currency}")

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

    def _update_item(existing_data_dict: dict, i: Any, last_data: dict):
        if existing_data_dict[i]['price'] != last_data[i]['price']:
            price = existing_data_dict[i]['price']
            new_price = last_data[i]['price']
            change  = round(float(new_price - price), 2)
            percent = float(f'{round(float((change / new_price) * 100 if price != 0 else 0), 2)}'.replace('-', ' '))
            symbol  = "" if change == 0 else "▲" if change >= 0 else "▼"
            color   = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
            last_update = last_data[i].get('last_update', None)
            change = float(str(change).replace('-', ' '))

            if not last_update:
                existing_data_dict[i].update({
                    'price': new_price,
                    'change': change,
                    'percent': percent,
                    'color': color,
                    'symbol': symbol,
                    'last_update': last_update
                })
            else:
                existing_data_dict[i].update({
                    'price': new_price,
                    'change': change,
                    'percent': percent,
                    'color': color,
                    'symbol': symbol,
                })

    try:
        monitor_class = None

        for monitor in monitor_classes:
            if monitor.get(provider.name) and currency in monitor.get(provider.name)['currency']:
                monitor_class = monitor[provider.name]['provider']

        if monitor_class is not None:
            data = monitor_class(url=provider.provider, currency=currency).get_values()
            if db is not None:
                key = f'{currency}:{provider.name}'
                cache = Cache(db)

                existing_data = cache.get_data(key)

                if not existing_data:
                    cache.set_data(key, json.dumps(data), db.ttl)

                existing_data_dict = json.loads(cache.get_data(key))
                for name in existing_data_dict:
                    if not name == 'last_update' and not name == 'banks':
                        if name in existing_data_dict and name in data:
                            _update_item(existing_data_dict, name, data)
                    else:
                        if name == 'banks' and name in data:
                            for i in range(len(existing_data_dict[name])):
                                _update_item(existing_data_dict[name], i, data[name])
                        elif name == 'last_update':
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