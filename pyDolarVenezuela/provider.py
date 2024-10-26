from typing import Union, Any, List, Dict
from datetime import datetime
from .exceptions import MonitorNotFound, CurrencyNotFound, DatabaseNotDefined
from .providers import AlCambio, BCV, CriptoDolar, DolarToday, ExchangeMonitor, EnParaleloVzla, Italcambio
from .data import DatabaseSettings, MonitorModel
from .models import Page, Monitor, HistoryPrice, LocalDatabase, Database
from .storage import Cache
from .pages import (
    AlCambio as A,
    BCV as B,
    CriptoDolar as C,
    DolarToday as D,
    ExchangeMonitor as E,
    EnParaleloVzla as EP,
    Italcambio as I
)
from .utils.time import standard_time_zone

monitor_classes = {
    A.name: {'currency': A.currencies, 'provider': AlCambio},
    B.name: {'currency': B.currencies, 'provider': BCV},
    C.name: {'currency': C.currencies, 'provider': CriptoDolar},
    D.name: {'currency': D.currencies, 'provider': DolarToday},
    E.name: {'currency': E.currencies, 'provider': ExchangeMonitor},
    EP.name: {'currency': EP.currencies, 'provider': EnParaleloVzla},
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
        self.key      = f'{page.name}:{currency}'
        
        if self.currency not in page.currencies:
            raise CurrencyNotFound(f"Tipo de moneda no encontrado. Debe ser USD o EUR. No '{currency}'")
        
        self.page = page
        self.database = database

        if self.database is not None:
            self._connection = DatabaseSettings(self.database)
    
    def _load_data(self) -> Union[List[Monitor], List[Dict[str, Any]]]:
        """
        Extrae los datos y si la base de datos está declarada, actualizará cada monitor en la página que estás solicitando.
        """
        monitor_class = monitor_classes.get(self.page.name).get('provider')
        data = [Monitor(**item) for item in monitor_class.get_values(currency=self.currency)]

        if self.database is not None:
            self.page_id = self._connection.get_or_create_page(self.page)
            self.currency_id = self._connection.get_or_create_currency(self.currency)

            if not self._connection.is_monitor_exists(self.page_id, self.currency_id):
                self._connection.create_monitors(self.page_id, self.currency_id, data)
            else:
                for new_monitor in data:
                    if not self._connection.is_monitor_exists_by_key(self.page_id, self.currency_id, new_monitor.key):
                        self._connection.create_monitor(self.page_id, self.currency_id, new_monitor)
                    else:
                        old_monitor = self._connection.get_monitor_by_key(self.page_id, self.currency_id, new_monitor.key)
                        old_last_update = old_monitor.last_update
                        new_last_update = new_monitor.last_update

                        if self.page.name in [B.name, EP.name, A.name, E.name]:
                            if self.page.name == B.name:
                                if old_last_update.date() != new_last_update.date():
                                    self._update_item(old_monitor, new_monitor)
                            else:
                                if old_last_update.astimezone(standard_time_zone) != new_last_update:
                                    self._update_item(old_monitor, new_monitor)
                        else:
                            if old_monitor.price != new_monitor.price and new_monitor.price > 0:
                                self._update_item(old_monitor, new_monitor)
                
            data = self._connection.get_monitors(self.page_id, self.currency_id)
            if not data:
                raise MonitorNotFound('No se pudo obtener los datos de la base de datos.')
        return data
    
    def _update_item(self, old_monitor: MonitorModel, new_monitor: Monitor) -> None:
        """
        Actualiza el objecto Monitor en la base de datos.

        Args:
        - old_monitor: Monitor Antiguo.
        - new_monitor: Monitor nuevo. Datos obtenidos recientes.
        """
        old_price = old_monitor.price
        new_price = new_monitor.price

        change = round(float(new_price) - float(old_price), 2)
        data = {
            'price': new_price,
            'price_old': old_price,
            'last_update': new_monitor.last_update,
            'change': change,
            'percent': float(f'{round(float((change / new_price) * 100 if old_price != 0 else 0), 2)}'.replace('-', ' ')),
            'color': "red" if new_price < old_price else "green" if new_price > old_price else "neutral",
            'symbol': "▲" if new_price > old_price else "▼" if new_price < old_price else ""
        }
        
        if old_monitor.image != new_monitor.image:
            data.update({'image': new_monitor.image})
        data.update({'change': float(str(data.get('change')).replace('-', ' '))})

        self._connection.update_monitor(old_monitor.id, data)
        self._connection.add_price_history(old_monitor.id, data['price'], data['last_update'])
    
    def get_values_specifics(self, cache: Union[Cache, None], type_monitor: str = None) -> Union[List[Monitor], Monitor]:
        """
        Obtiene los valores específicos de un monitor o de todos los monitores.

        Args:
        - type_monitor: El tipo de monitor a obtener.
        """
        try:
            if cache is None or not cache.get(self.key):
                data = self._load_data()
                if cache is not None:
                    cache.set(self.key, data)
            else:
                data = cache.get(self.key)
            
            if self.database is not None:
                data = [Monitor(**model_to_dict(monitor, exclude=['id', 'page_id', 'currency_id'])) for monitor in data]
            
            if not type_monitor:
                return data

            type_monitor_lower = type_monitor.lower()
            monitor_data = next((monitor for monitor in data if monitor.key == type_monitor_lower), None)
            if not monitor_data:
                raise MonitorNotFound('El monitor que intentó obtener. No se encuentra, comprueba cómo se encuentra el key.')
            
            return monitor_data
        except Exception as e:
            raise e
    
    def get_prices_history(self, type_monitor: str, start_date: str, end_date: Union[str, datetime] = datetime.now()) -> List[HistoryPrice]:
        """
        Obtiene el historial de precios de un monitor específico.

        Args:
        - type_monitor: El tipo de monitor a obtener.
        - start_date: Fecha de inicio del historial.
        - end_date: Fecha de fin del historial.
        """
        try:
            if not self.database:
                raise DatabaseNotDefined('La base de datos no está declarada.')
            
            start_date  = datetime.strptime(start_date, "%d-%m-%Y").date()
            end_date    = datetime.strptime(end_date, "%d-%m-%Y").date() if isinstance(end_date, str) else end_date.date()
            page_id     = self._connection.get_or_create_page(self.page)
            currency_id = self._connection.get_or_create_currency(self.currency)
            
            data = self._connection.get_date_range_history(page_id, currency_id, type_monitor, start_date, end_date)
            data = [HistoryPrice(**model_to_dict(monitor, exclude=['id', 'monitor_id'])) for monitor in data]
            
            return data
        except ValueError as e:
            raise ValueError('La fecha proporcionada no es válida. DD-MM-YYYY')
        except Exception as e:
            raise e
    
    def get_daily_price_monitor(self, type_monitor: str, date: str) -> List[HistoryPrice]:
        """
        Obtiene los precios de un monitor específico en una fecha especifica.

        Args:
        - type_monitor: El tipo de monitor a obtener.
        - date: Fecha de la que se desea obtener los precios.
        """
        try:
            if not self.database:
                raise DatabaseNotDefined('La base de datos no está declarada.')
            
            date        = datetime.strptime(date, "%d-%m-%Y").date()
            page_id     = self._connection.get_or_create_page(self.page)
            currency_id = self._connection.get_or_create_currency(self.currency)
            
            data = self._connection.get_prices_monitor_one_day(page_id, currency_id, type_monitor, date)
            data = [HistoryPrice(**model_to_dict(monitor, exclude=['id', 'monitor_id'])) for monitor in data]
            
            return data
        except ValueError as e:
            raise ValueError('La fecha proporcionada no es válida. DD-MM-YYYY')
        except Exception as e:
            raise e