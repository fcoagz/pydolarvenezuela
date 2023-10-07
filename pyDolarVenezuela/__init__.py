from pyDolarVenezuela import pages
from pyDolarVenezuela import network
from pyDolarVenezuela.tools import currency_converter
from .provider import Provider

import json
from colorama import Fore

version = '1.3.6'

def check_dependence_version():
    response = network.get("https://pypi.org/pypi/pydolarvenezuela/json")
    latest_version = json.loads(response)["info"]["version"]

    if version != latest_version:
        print(f"{Fore.GREEN}New version: {latest_version}.{Fore.RESET} {Fore.RED}Current version {version}.{Fore.RESET} write the following command: pip install --upgrade pyDolarVenezuela\n")

check_dependence_version()

def getdate():
    from pyDolarVenezuela.tools import TimeDollar
    t = TimeDollar()

    return t.get_time_zone()

class Monitor:
    def __init__(self, provider: pages.Monitor, ) -> None:
        """
        La clase Monitor permite consultar los precios del dólar en diversos monitores en Venezuela. \n
        El método `get_value_monitors` permite acceder a los datos almacenados en el diccionario.
        """
        if not isinstance(provider, pages.Monitor):
            raise TypeError("El parámetro debe ser un objeto del tipo Monitor.")
        
        self.provider = provider

    def get_value_monitors(self, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        """
        El parámetro `monitor_code` indica el código del monitor del cual se desea obtener información, \
        mientras que el parámetro `prettify` permite mostrar los precios en formato de moneda con el símbolo de Bolívares. \
        Si se proporciona un nombre de propiedad válido, se devolverá el valor correspondiente para ese monitor.
        """
        return Provider.select_monitor(self.provider, monitor_code, name_property, prettify)

__all__ = ['pages', 'currency_converter', 'getdate', 'Monitor']