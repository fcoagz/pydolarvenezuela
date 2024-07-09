from typing import Any, List, Dict, Literal, Union
from datetime import timedelta
from . import pages
from .models import Page, LocalDatabase, Database
from .provider import Provider
from .utils import currency_converter
from .utils import get_time_zone as getdate
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
    def __init__(self, provider: Page, currency: Literal['USD', 'EUR'] = 'USD', db: Union[LocalDatabase, Database] = None, ttl: timedelta = timedelta(minutes=10)) -> None:
        """
        La clase `Monitor` proporciona funcionalidades para consultar los precios de diversos monitores en Venezuela.

        Args:
        - provider: La página de la que se accederán los datos.
        - currency: La moneda en la que se expresarán los precios. Puede ser `USD` o `EUR`. Por defecto es `USD`.
        - db: La base de datos en la que se almacenarán los datos. Por defecto es `None`.
        - ttl: Tiempo de vida del cache. Por defecto es `360seg`
        """

        if CheckVersion.check:
            CheckVersion._check_dependence_version()
        if not isinstance(provider, Page):
            raise TypeError("The parameter must be an object of type Monitor.")
        
        from .storage import Cache
        
        self.cache = Cache(ttl=ttl)
        self.key   = f'{provider.name}:{currency}'
        self.provider = provider
        self.currency = currency.lower()
        self.db       = db
        self.select_monitor = Provider(provider, currency, db)
    
    def get_all_monitors(self) -> List[Dict[str, Any]]:
        """
        El método `get_all_monitors` permite obtener todos los monitores disponibles.
        """
        if not self.cache.get(self.key):
            result = self.select_monitor.get_values_specifics()
            self.cache.set(self.key, result)
        return self.cache.get(self.key)

    def get_value_monitors(self,
                           type_monitor: str = None,
                           property: Literal['title', 'price', 'last_update'] = None,
                           prettify: bool = False) -> Union[List[Dict[str, Any]], Dict[str, Any], Any]:
        """
        El método `get_value_monitors` permite acceder a los datos extraídos de los monitores.

        Args:
        - type_monitor: El código del monitor del cual se desea obtener información. Por defecto es `None`.
        - property: El nombre de la propiedad específica del diccionario de la información del monitor extraído que se desea obtener. Por defecto es `None`.
        - prettify: Si es True, muestra los precios en formato de moneda con el símbolo de Bolívares. Por defecto es `False`.
        """ 
        if not self.cache.get(self.key):
            result = self.select_monitor.get_values_specifics(type_monitor, property, prettify)
            self.cache.set(self.key, result)
        return self.cache.get(self.key)