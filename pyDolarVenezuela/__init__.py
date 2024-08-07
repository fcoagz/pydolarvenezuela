from typing import List, Literal, Union
from datetime import datetime, timedelta
from . import pages
from .models import Page, LocalDatabase, Database, Monitor as MonitorModel, HistoryPrice
from .provider import Provider
from .utils.calculator import currency_converter
from .utils.time import get_time_zone as getdate
from .version import CheckVersion, __version__

__all__ = (
    "Monitor",
    "pages",
    "LocalDatabase",
    "Database",
    "getdate",
    "currency_converter",
    "CheckVersion",
    "__version__"
)

class Monitor:
    def __init__(self,
                provider: Page,
                currency: Literal['USD', 'EUR'] = 'USD',
                db: Union[LocalDatabase, Database] = None,
                ttl: Union[timedelta, int, None] = None) -> None:
        """
        La clase `Monitor` proporciona funcionalidades para consultar los precios de diversos monitores en Venezuela.

        Args:
        - provider: La página de la que se accederán los datos.
        - currency: La moneda en la que se expresarán los precios. Puede ser `USD` o `EUR`. Por defecto es `USD`.
        - db: La base de datos en la que se almacenarán los datos. Por defecto es `None`.
        - ttl: Tiempo de vida del cache. Por defecto es `None`.
        """

        if CheckVersion.check:
            CheckVersion._check_dependence_version()
        
        from .storage import Cache
        
        if ttl is None:
            self.cache = ttl
        else:
            self.cache = Cache(ttl=ttl)
            
        self.provider = provider
        self.currency = currency.lower()
        self.db       = db
        self.select_monitor = Provider(provider, currency, db)
    
    def get_all_monitors(self) -> List[MonitorModel]:
        """
        El método `get_all_monitors` permite obtener todos los monitores disponibles.
        """
        result = self.select_monitor.get_values_specifics(self.cache)
        return result

    def get_value_monitors(self, type_monitor: str) -> MonitorModel:
        """
        El método `get_value_monitors` permite acceder a los datos extraídos de los monitores.

        Args:
        - type_monitor: El código del monitor del cual se desea obtener información. 
        """ 
        result = self.select_monitor.get_values_specifics(self.cache, type_monitor)
        return result
    
    def get_daily_price_monitor(self, type_monitor: str, date: str) -> List[HistoryPrice]:
        """
        El método `get_daily_price_monitor` permite obtener los precios de un monitor específico en una fecha determinada.\n\n

        El formato debe ser `dd-mm-yyyy`.

        Args:
        - type_monitor: El código del monitor del cual se desea obtener información.
        - date: Fecha de la cual se desea obtener los precios.
        """
        result = self.select_monitor.get_daily_price_monitor(type_monitor, date)
        return result

    def get_prices_history(self, type_monitor: str, start_date: str, end_date: Union[str, datetime] = datetime.now()) -> List[HistoryPrice]:
        """
        El método `get_prices_history` permite obtener el historial de precios de un monitor específico.\n\n

        El formato debe ser `dd-mm-yyyy`.

        Args:
        - type_monitor: El código del monitor del cual se desea obtener información.
        - start_date: Fecha de inicio del historial.
        - end_date: Fecha de fin del historial. Por defecto es la fecha actual.
        """
        result = self.select_monitor.get_prices_history(type_monitor, start_date, end_date)
        return result