import json
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela
from .dpedidos import Dpedidos

from ..data.redis import Cache
from ..models.database import Redis
from ..models.pages import Monitor
from ..pages import BCV as B, CriptoDolar as C, Dpedidos as D, ExchangeMonitor as E, iVenezuela as I 

monitor_classes = {
    'usd': {
        B.name: BCV,
        C.name: CriptoDolar,
        E.name: ExchangeMonitor,
        D.name: Dpedidos,
        I.name: iVenezuela
    },
    'eur': {
        B.name: BCV,
        C.name: CriptoDolar,
        E.name: ExchangeMonitor
    }
}

def select_monitor(provider: Monitor, db: Redis, **kwargs):
    currency = kwargs.get('currency')
    monitor_code = kwargs.get('monitor_code')
    name_property = kwargs.get('name_property')
    prettify = kwargs.get('prettify', False)

    if currency not in ['usd', 'eur']:
        raise ValueError(f"The currency type must be 'usd' or 'eur', not {currency}")

    try:
        monitor_class = monitor_classes.get(currency).get(provider.name)
        if monitor_class is not None:
            if db is not None:
                response = monitor_class(provider.provider, currency).get_values()

                key = f'{currency}:{provider.name}'
                cache = Cache(db)

                existing_data = cache.get_data(key)

                if not existing_data:
                    cache.set_data(key, json.dumps(response), db.ttl)
                else:
                    existing_data_dict: dict[str, dict] = json.loads(existing_data)
                    for name in existing_data_dict:
                        if not name == 'last_update':
                            if name in existing_data_dict and name in response:
                                if existing_data_dict[name]['price'] != response[name]['price']:
                                    price = existing_data_dict[name]['price']
                                    new_price = response[name]['price']
                                    change  = round(float(new_price - price), 2)
                                    percent = f'{round(float((change / new_price) * 100 if price != 0 else 0), 2)}%'
                                    symbol  = "" if change == 0 else "▲" if change >= 0 else "▼"
                                    color   = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
                                    last_update = None if provider.name == B.name else response[name]['last_update']

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
                            existing_data_dict[name] = response[name]
                            
                cache.set_data(key, json.dumps(existing_data_dict), db.ttl)
                existing_data_dict: dict[str, dict] = json.loads(
                    cache.get_data(key)
                )

                if not monitor_code:
                    return existing_data_dict
                
                try:
                    monitor_data = existing_data_dict[monitor_code.lower()]
                    if name_property:
                        value = monitor_data[name_property]
                        return f'Bs. {value}' if prettify and name_property == 'price' else value
                    return monitor_data
                except KeyError:
                    raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")

            return monitor_class(provider.provider, currency).get_values(
                monitor_code=monitor_code,
                name_property=name_property, 
                prettify=prettify
            )
        else:
            raise ValueError("Provider not supported")
    except Exception as e:
        raise e