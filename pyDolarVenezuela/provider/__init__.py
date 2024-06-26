from typing import Union, Any, List, Dict
from .alcambio import AlCambio
from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .italcambio import Italcambio

from ..data.main import SettingsDB
from ..data.models import Monitor as SchemaMonitorDB
from ..models.pages import Page
from ..models.monitor import Monitor
from ..models.database import LocalDatabase, Database
from ..pages import AlCambio as A, BCV as B, CriptoDolar as C, ExchangeMonitor as E, Italcambio as I

monitor_classes = {
    A.name: {'currency': A.currencies, 'provider': AlCambio},
    B.name: {'currency': B.currencies, 'provider': BCV},
    C.name: {'currency': C.currencies, 'provider': CriptoDolar},
    E.name: {'currency': E.currencies, 'provider': ExchangeMonitor},
    I.name: {'currency': I.currencies, 'provider': Italcambio},
}

def model_to_dict(model, exclude: List[str] = None) -> Dict[Any, Any]:
    """
    Convierte una instancia del modelo de SQLAlchemy en un diccionario,
    excluyendo los atributos especificados.
    
    Args:
    - model: La instancia del modelo de SQLAlchemy.
    - exclude: Lista de nombres de atributos a excluir del diccionario.
    """
    exclude = exclude or []
    return {
        column.name: getattr(model, column.name)
        for column in model.__table__.columns
        if column.name not in exclude
    }

class Provider:
    def __init__(self,
                page: Page, 
                currency: str, 
                database: Union[LocalDatabase, Database] = None) -> None:
        if currency.lower() not in page.currencies:
            raise ValueError(f"The currency type must be 'usd', 'eur'..., not {currency}")
        
        self.page = page
        self.currency = currency.lower()
        self.database = database

        if self.database is not None:
            self._connection = SettingsDB(self.database)

    def _load_data(self):
        monitor_class = monitor_classes.get(self.page.name).get('provider')
        values = monitor_class(url=self.page.provider, currency=self.currency).get_values()

        if self.database is not None:
            self.page_id = self._connection.get_or_create_page(self.page)
            self.currency_id = self._connection.get_or_create_currency(self.currency)

            self._connection.create_monitors(self.page_id, self.currency_id, [
                Monitor(**item) if not item.get('banks') else Monitor(**bank)
                for item in values
                for bank in item.get('banks', [item]) 
            ])

            old_data = self._connection.get_monitors(self.page_id, self.currency_id)
            new_data = [
                    Monitor(**item) if not item.get('banks') else Monitor(**bank)
                    for item in values
                    for bank in item.get('banks', [item]) 
                ]
            for i in range(len(new_data)):
                self._update_item(old_data, new_data, i)

            values = self._connection.get_monitors(self.page_id, self.currency_id)
        return values 
    
    def _update_price(self, old_data: List[SchemaMonitorDB], new_data: List[Monitor], index: int, index_extra: int = None) -> None:
        """
        Actualiza el precio y otros atributos en `old_data` basándose en la información de `new_data`.

        Args:
        - old_data: la lista de elementos de datos antiguos.
        - new_data: la lista de nuevos elementos de datos.
        - index: El índice del elemento a actualizar.
        - index_extra: Una clave opcional para acceder a los datos en `new_data`. Por defecto es `None`. 
        Si no se proporciona, se usará el valor de `index`.
        """        
        index_key = index_extra if index_extra is not None else index

        old_price = old_data[index].price
        new_price = new_data[index_key].price
        price_old = new_data[index_key].price_old # Valor preciso
        change    = round(float(new_price - old_price), 2)
        percent   = float(f'{round(float((change / new_price) * 100 if old_price != 0 else 0), 2)}'.replace('-', ' '))
        symbol    = "" if change == 0 else "▲" if change >= 0 else "▼"
        color     = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
        last_update = new_data[index_key].last_update
        change = float(str(change).replace('-', ' '))
        image  = new_data[index_key].image

        self._connection.update_monitor(old_data[index].id, Monitor(
            key=old_data[index].key,
            title=old_data[index].title,
            price=new_price,
            price_old=price_old,
            last_update=last_update,
            image=image,
            percent=percent,
            change=change,
            color=color,
            symbol=symbol
        ))

    def _update_item(self, old_data: List[SchemaMonitorDB], new_data: List[Monitor], i: int) -> None:
        """
        Actualiza un elemento en la lista `old_data` con el elemento `new_data` correspondiente en el índice `i`.

        Args:
        - old_data: la lista de elementos de datos antiguos.
        - new_data: la lista de nuevos elementos de datos.
        - i: El índice del elemento a actualizar.
        """
        title_items = [item.title for item in old_data]
        if new_data[i].title in title_items:
            index_old_data = title_items.index(new_data[i].title)
            if old_data[index_old_data].price != new_data[i].price:
                # 'index_old_data' es la posición en old_data y 'i' es la posición en new_data.
                self._update_price(old_data, new_data, index_old_data, i)
        else:
            self._connection.create_monitor(self.page_id, Monitor(**new_data[i]))

    def get_values_specifics(self,
                              type_monitor: str = None,
                              property: str = None,
                              prettify: bool = False) -> Union[List[Dict[str, Any]], Dict[str, Any], Any]:
        data = self._load_data()
        
        if self.database is not None:
            data = [model_to_dict(monitor, exclude=['id', 'page_id', 'currency_id']) for monitor in data]

        if not type_monitor:
            return data

        type_monitor_lower = type_monitor.lower()

        try:
            monitor_data = next((monitor for monitor in data if monitor.key == type_monitor_lower), None)

            if not monitor_data:
                raise KeyError(f'Type monitor "{type_monitor}" not found.')

            if property:
                property_value = getattr(monitor_data, property, None)
                if property_value is None:
                    raise KeyError(f'Property "{property}" not found in type monitor "{type_monitor}".')
                
                if prettify and property == 'price':
                    return f'Bs. {property_value}'
                return property_value

            return monitor_data
        except KeyError as e:
            raise KeyError(f'{e} https://github.com/fcoagz/pyDolarVenezuela')
        except Exception as e:
            raise e