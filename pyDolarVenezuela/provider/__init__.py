import json
from typing import Any
from dataclasses import asdict
from .alcambio import AlCambio
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .italcambio import Italcambio

from ..data.redis import Cache
from ..models.monitor import Monitor
from ..models.database import Redis
from ..models.pages import Page
from ..pages import AlCambio as A, BCV as B, CriptoDolar as C, ExchangeMonitor as E, Italcambio as I

monitor_classes = {
    A.name: {'currency': A.currencies, 'provider': AlCambio},
    B.name: {'currency': B.currencies, 'provider': BCV},
    C.name: {'currency': C.currencies, 'provider': CriptoDolar},
    E.name: {'currency': E.currencies, 'provider': ExchangeMonitor},
    I.name: {'currency': I.currencies, 'provider': Italcambio},
}

class Provider:
    def __init__(self,
                page: Page, 
                currency: str, 
                db: Redis = None) -> None:
        if currency.lower() not in page.currencies:
            raise ValueError(f"The currency type must be 'usd', 'eur'..., not {currency}")
        
        self.page = page
        self.currency = currency.lower()
        self.db = db

        if self.db is not None:
            self._redis = Cache(self.db)

    def _load_data(self):
        monitor_class = monitor_classes.get(self.page.name).get('provider')
        values = monitor_class(url=self.page.provider, currency=self.currency).get_values()

        if self.db is not None:
            key = f'{self.currency}:{self.page.name}'
            
            if not self._redis.get_data(key):
                self._redis.set_data(key, json.dumps(values), self.db.ttl)

            old_data = json.loads(self._redis.get_data(key))
            for property in old_data:
                if property not in ('banks', 'last_update'):
                    try:
                        self._update_item(old_data, values, property)
                    except KeyError:
                        pass
                elif property == 'banks': # Comparación de propiedades de los datos BCV
                    banks = values[property]
                    for i, bank in enumerate(old_data[property]):
                        if i < len(banks) and bank['title'] == banks[i]['title']:
                            self._update_item(old_data[property], banks, i)
                elif property == 'last_update':
                    old_data[property] = values[property]

            self._redis.set_data(key, json.dumps(old_data), self.db.ttl)
            values = json.loads(self._redis.get_data(key))
            
        return values 
    
    def _update_item(self, old_data: dict, new_data: dict, i: Any):
        """
        Evalúa la estructura de cada monitor en `old_data`. Elimina los atributos que sean `None` (Cada estructura es diferente según el proveedor) y realiza los cálculos necesarios.

        Estructura inicial (para la primera vez):
        ```python
        class Monitor:
            title: str  
            price: float  
            price_old: Optional[float] = None 
            last_update: Optional[str] = None  
            image: Optional[str] = None  
            percent: Optional[float] = 0.0
            change: Optional[float] = 0.0  
            color: Optional[str] = "neutral" 
            symbol: Optional[str] = "" 
        ```
        """
        structure_monitor = asdict(Monitor(**old_data[i]))
        for key in list(structure_monitor.keys()):
            if structure_monitor[key] is None:
                del structure_monitor[key]
        old_data[i] = structure_monitor
        
        if old_data[i]['price'] != new_data[i]['price']:
            old_price = old_data[i]['price']
            new_price = new_data[i]['price']
            price_old = new_data[i].get('price_old', None) # Valor preciso
            change    = round(float(new_price - old_price), 2)
            percent   = float(f'{round(float((change / new_price) * 100 if old_price != 0 else 0), 2)}'.replace('-', ' '))
            symbol    = "" if change == 0 else "▲" if change >= 0 else "▼"
            color     = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
            last_update = new_data[i].get('last_update', None)

            change = float(str(change).replace('-', ' '))

            old_data[i].update({
                'price': new_price,
                'change': change,
                'percent': percent,
                'color': color,
                'symbol': symbol,
            })
            
            # Comprueba si los atributos tienen valor. se agregan y/o actualizan
            if last_update and price_old:
                old_data[i].update({
                    'price_old': price_old,
                    'last_update': last_update
                })
                
            elif last_update: 
                old_data[i].update({
                    'last_update': last_update
                })

    def _get_values_specifics(self, type_monitor: str = None, property: str = None, prettify: bool = False):
        data = self._load_data()
        if not type_monitor:
            return data
        
        try:
            monitor_data = data[type_monitor.lower()]
            if property:
                if property == 'last_update' and self.page.name == B.name:
                    return monitor_data[property]
                value = monitor_data[property]
                return f'Bs. {value}' if prettify and property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError('Property not found. https://github.com/fcoagz/pyDolarVenezuela')
        except Exception as e:
            raise e