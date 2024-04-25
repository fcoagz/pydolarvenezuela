import json
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela
from .dpedidos import Dpedidos

from ..data.redis import Cache
from ..models.database import Redis
from ..models.pages import Monitor
from ..models.pages import BCV as B, CriptoDolar as C, Dpedidos as D, ExchangeMonitor as E, iVenezuela as I 

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

                if not cache.get_data(key):
                    cache.set_data(key, json.dumps(response), db.ttl)
                
                get_data = dict(json.loads(cache.get_data(key)))
                for name in get_data:
                    if not name == 'last_update':
                        price   = get_data[name]['price']
                        change  = price - response[name]['price']
                        percent = f'{(change / price) * 100 if price != 0 else 0}%'
                        symbol  = "" if change == 0 else "▲" if change >= 0 else "▼"
                        color   = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
                        
                        get_data[name].update({
                            'price': price,
                            'change': change,
                            'percent': percent,
                            'color': color,
                            'symbol': symbol
                        })
                        
                    cache.set_data(key, json.dumps(get_data), db.ttl)
                
                if not monitor_code:
                    return get_data
                
                try:
                    monitor_data = get_data[monitor_code.lower()]
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