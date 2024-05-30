import json
from typing import Literal
from colorama import Fore

from . import network
from .models.pages import Page
from .data.redis import Redis
from .utils import get_time_zone as getdate, currency_converter
from .provider import Provider

version = '1.6.0'
"""
Versión actual de la biblioteca    
"""

class CheckVersion:
    """
    Verificar actualización de la biblioteca    
    ```py
    check: bool = True
    ```
    """
    check = True

    @classmethod
    def _check_dependence_version(self):
            response = network.get("https://pypi.org/pypi/pydolarvenezuela/json")
            latest_version = json.loads(response)["info"]["version"]

            if version != latest_version:
                print(f"{Fore.GREEN}New version: {latest_version}.{Fore.RESET} {Fore.RED}Current version {version}.{Fore.RESET} write the following command: pip install --upgrade pyDolarVenezuela\n")

class Monitor:
    def __init__(self, provider: Page, currency: Literal['USD', 'EUR'] = 'USD', db: Redis = None) -> None:
        """
        La clase `Monitor` proporciona funcionalidades para consultar los precios de diversos monitores en Venezuela.

        Parámetros:
        - `provider`: La página de la que se accederán los datos.
        - `currency`: La moneda en la que se expresarán los precios. Puede ser `USD` o `EUR`. Por defecto es `USD`.
        - `db`: Base de datos con Redis. 
        """

        if CheckVersion.check:
            CheckVersion._check_dependence_version()
        if not isinstance(provider, Page):
            raise TypeError("The parameter must be an object of type Monitor.")
        
        self.provider = provider
        self.currency = currency.lower()
        self.db       = db
        self.select_monitor = Provider(provider, currency, db)
    
    def get_all_monitors(self):
        return self.select_monitor._get_values_specifics()

    def get_value_monitors(self, type_monitor: str = None, property: Literal['title', 'price', 'last_update'] = None, prettify: bool = False):
        """
        El método `get_value_monitors` permite acceder a los datos extraídos de los monitores.

        Parámetros:
        - `type_monitor`: El código del monitor del cual se desea obtener información. Por defecto es `None`.
        - `property`: El nombre de la propiedad específica del diccionario de la información del monitor extraído que se desea obtener. Por defecto es `None`.
        - `prettify`: Si es True, muestra los precios en formato de moneda con el símbolo de Bolívares. Por defecto es `False`.
        """ 
        return self.select_monitor._get_values_specifics(
            type_monitor,
            property,
            prettify
        )