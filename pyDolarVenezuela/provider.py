from typing import Union, Any, List, Dict
from .providers import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
from .data import SettingsDB, MonitorModel
from .models import Page, Monitor, LocalDatabase, Database
from .pages import AlCambio as A, BCV as B, CriptoDolar as C, ExchangeMonitor as E, Italcambio as I

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
    def __init__(self, page: Page, currency: str, database: Union[LocalDatabase, Database] = None) -> None:
        """
        Clase `Provider` para manipulación de datos.

        Args:
        - page: La página de la que se accederán los datos.
        - currency: La moneda en la que se expresarán los precios.
        - database: La base de datos en la que se almacenarán los datos.
        """
        
        self.currency = currency.lower()
        
        if self.currency not in page.currencies:
            raise ValueError(f"The currency type must be 'usd', 'eur'..., not {currency}")
        
        self.page = page
        self.database = database

        if self.database is not None:
            self._connection = SettingsDB(self.database)
    
    def _load_data(self) -> Union[List[Monitor], List[Dict[str, Any]]]:
        """
        Extrae los datos y si la base de datos está declarada, actualizará cada monitor en la página que estás solicitando.
        """
        monitor_class = monitor_classes.get(self.page.name).get('provider')
        values = monitor_class(url=self.page.provider, currency=self.currency).get_values()

        if self.database is not None:
            self.page_id = self._connection.get_or_create_page(self.page)
            self.currency_id = self._connection.get_or_create_currency(self.currency)
            self._connection.create_monitors(self.page_id, self.currency_id, [Monitor(**item) for item in values])

            old_data = self._connection.get_monitors(self.page_id, self.currency_id)
            new_data = [Monitor(**item) for item in values]
            title_items = [item.title for item in old_data]
            
            for i in range(len(new_data)):
                if new_data[i].title not in title_items:
                    self._connection.create_monitor(self.page_id, self.currency_id, new_data[i])
                else:
                    index_old_data = title_items.index(new_data[i].title)
                
                    if self.page.name not in [I.name, E.name]:
                        if old_data[index_old_data].last_update != new_data[i].last_update:
                            self._update_item(old_data, new_data, i, index_old_data)
                    else:
                        if old_data[index_old_data].price != new_data[i].price:
                            self._update_item(old_data, new_data, i, index_old_data)
            
            values = self._connection.get_monitors(self.page_id, self.currency_id)
        return values
    
    def _update_item(self, old_data: List[MonitorModel], new_data: List[Monitor], index: int, index_extra: int = None) -> None:
        """
        Actualiza el objecto Monitor en la base de datos.

        Args:
        - old_data: Lista de monitores antiguos.
        - new_data: Lista de nuevos monitores.
        - index: Índice del monitor a actualizar.
        - index_extra: Índice extra del monitor a actualizar.
        """
        index_key = index_extra if index_extra is not None else index

        old_price = old_data[index_key].price
        new_price = new_data[index].price
        price_old = new_data[index].price_old
        change    = round(float(new_price - old_price), 2)
        percent   = float(f'{round(float((change / new_price) * 100 if old_price != 0 else 0), 2)}'.replace('-', ' '))
        symbol    = "" if change == 0 else "▲" if change >= 0 else "▼"
        color     = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
        last_update = new_data[index_key].last_update
        change = float(str(change).replace('-', ' '))
        image  = new_data[index_key].image

        monitor = Monitor(
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
        )
        
        self._connection.update_monitor(old_data[index].id, monitor)
    
    def get_values_specifics(self, type_monitor: str = None, property: str = None, prettify: bool = False) -> Union[List[Dict[str, Any]], Dict[str, Any], Any]:
        """
        Obtiene los valores específicos de un monitor o de todos los monitores.

        Args:
        - type_monitor: El tipo de monitor a obtener.
        - property: La propiedad del monitor a obtener.
        - prettify: Si se debe formatear el precio del monitor `38.40` a `Bs. 38.40`.
        """
        data = self._load_data()
        
        if self.database is not None:
            data = [model_to_dict(monitor, exclude=['id', 'page_id', 'currency_id']) for monitor in data]
        if not type_monitor:
            return data

        type_monitor_lower = type_monitor.lower()
        try:
            monitor_data = next((monitor for monitor in data if monitor.get('key') == type_monitor_lower), None)

            if not monitor_data:
                raise KeyError(f'Type monitor "{type_monitor}" not found.')

            if property:
                property_value = monitor_data.get(property)
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