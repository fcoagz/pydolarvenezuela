import json
from colorama import Fore
from . import network

__version__ = '1.6.2'
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
        """
        Obtenga la última versión de un paquete PyPI.
        """
        response = network.get("https://pypi.org/pypi/pydolarvenezuela/json")
        latest_version = json.loads(response)["info"]["version"]

        if __version__ != latest_version:
            print(f"{Fore.GREEN}New version: {latest_version}.{Fore.RESET} {Fore.RED}Current version {__version__}.{Fore.RESET} write the following command: pip install --upgrade pyDolarVenezuela\n")