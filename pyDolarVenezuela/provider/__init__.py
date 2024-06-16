import json
from typing import Any, Union
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
                    for i in range(len(banks)):
                        self._update_item(old_data[property], banks, i)
                elif property == 'last_update':
                    old_data[property] = values[property]

            self._redis.set_data(key, json.dumps(old_data), self.db.ttl)
            values = json.loads(self._redis.get_data(key))
            
        return values 
    
    def _update_price(self, old_data: Union[list, dict], new_data: Union[list, dict], index: Any, index_extra: Any = None):
        """
        Actualiza el precio y otros atributos en `old_data` basándose en la información de `new_data`.

        Args:
        - `old_data`: El diccionario que contiene los datos antiguos a actualizar.
        - `new_data`: El diccionario que contiene los nuevos datos.
        - `index`: La clave para acceder a los datos en `old_data`.
        - `index_extra`: Una clave opcional para acceder a los datos en `new_data`. Por defecto es `None`. 
        Si no se proporciona, se usará el valor de `index`.
        """        
        index_key = index_extra if index_extra is not None else index

        old_price = old_data[index]['price']
        new_price = new_data[index_key]['price']
        price_old = new_data[index_key].get('price_old', None) # Valor preciso
        change    = round(float(new_price - old_price), 2)
        percent   = float(f'{round(float((change / new_price) * 100 if old_price != 0 else 0), 2)}'.replace('-', ' '))
        symbol    = "" if change == 0 else "▲" if change >= 0 else "▼"
        color     = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
        last_update = new_data[index_key].get('last_update', None)

        change = float(str(change).replace('-', ' '))

        old_data[index].update({
            'price': new_price,
            'change': change,
            'percent': percent,
            'color': color,
            'symbol': symbol,
        })
        
        # Comprueba si los atributos tienen valor. se agregan y/o actualizan
        if price_old is not None:
            old_data[index].update({
                'price_old': price_old
        })
         
        if last_update is not None: 
            old_data[index].update({
                'last_update': last_update
        })

    def _update_item(self, old_data: Union[list, dict], new_data: Union[list, dict], i: Any):
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
        
        if isinstance(i, str) or (isinstance(i, int) and i <= len(old_data) - 1):
            structure_monitor = asdict(Monitor(**old_data[i]))
            for key in list(structure_monitor.keys()):
                if structure_monitor[key] is None:
                    del structure_monitor[key]
            old_data[i] = structure_monitor

        # Ambos consultan si el precio es diferente para realizar cambios.
        # Hay diferentes datos que se distribuyeron como list, {str: dict}.
        if isinstance(i, int): # Actualiza los datos de 'old_data' con los datos de 'new_data' basándose en el título del item.
            title_items = [item['title'] for item in old_data]
            if new_data[i]['title'] in title_items:
                index_old_data = title_items.index(new_data[i]['title']) # Encuentra la posición donde se almacena el elemento en la lista
                if index_old_data < len(new_data) and old_data[index_old_data]['price'] != new_data[i]['price']:
                    # 'index_old_data' es la posición en old_data y 'i' es la posición en new_data.
                    self._update_price(old_data, new_data, index_old_data, i)
            else:
                old_data.append(new_data[i])
        else: # Actualiza los datos de 'old_data' con los datos de 'new_data' basándose en el key del item.
            if i in old_data: 
                if old_data[i]['price'] != new_data[i]['price']:
                    self._update_price(old_data, new_data, i)
            else:
                old_data[i] = new_data[i]

    def _get_values_specifics(self, type_monitor: str = None, property: str = None, prettify: bool = False):
        data = self._load_data()
        if not type_monitor:
            return data
        
        try:
            if self.page.name == B.name and type_monitor.lower() in [bank['title'].lower() for bank in data['banks']]:
                monitor_data = next((bank for bank in data['banks'] if bank['title'].lower() == type_monitor.lower()), None)
            else:
                monitor_data = data.get(type_monitor.lower())
            
            if not monitor_data:
                raise KeyError(f'Type monitor "{type_monitor}" not found.')

            if property:
                if property not in monitor_data:
                    raise KeyError(f'Property "{property}" not found in type monitor "{type_monitor}".')
                
                if property == 'last_update' and self.page.name == B.name:
                    return monitor_data[property]
                
                value = monitor_data[property]
                return f'Bs. {value}' if prettify and property == 'price' else value
            
            return monitor_data
        except KeyError as e:
            raise KeyError(f'{e} https://github.com/fcoagz/pyDolarVenezuela')
        except Exception as e:
            raise e