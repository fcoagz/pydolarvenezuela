from bs4 import BeautifulSoup
from dataclasses import asdict

from pyDolarVenezuela.time.functions import TimeDollar
from pyDolarVenezuela.module.dollar import InformationDollar
from pyDolarVenezuela.calculator.function import currency_converter
from pyDolarVenezuela.request import content
from pyDolarVenezuela.util import ExchangeMonitor

def _get_values_monitors(soup: BeautifulSoup):
    return [value for value in soup]

def _convert_specific_format(text: str, character: str = '_') -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

class Monitor(object):
    def __init__(self) -> None:
        """
        La clase Monitor permite consultar los precios del dólar en diversos monitores en Venezuela. \n
        El método `_screaped` carga los datos de los monitores a través del scraping de la página web de referencia, donde los datos son almacenados en un diccionario. \ 
        El método `get_value_monitors` permite acceder a los datos almacenados en el diccionario.
        """
        self.url = ExchangeMonitor + "/dolar-venezuela"
    
    def _scraped(self):
        response = content(self.url)
        soup = BeautifulSoup(response, "html.parser")
        time = TimeDollar()

        section_dolar_venezuela = soup.find_all("div", "col-xs-12 col-sm-6 col-md-4 col-tabla")
        _scraping_monitors = _get_values_monitors(section_dolar_venezuela)
        
        self.data = {}
        self.data['datetime'] = time.get_time_zone()

        for scraping_monitor in _scraping_monitors:
            result = scraping_monitor.find("div", "module-table module-table-fecha")

            name  = result.find("h6", "nombre").text
            price = str(result.find('p', "precio").text).replace(',', '.')

            if price.count('.') == 2:
                price = price.replace('.', '', 1)
            
            last_update = time.get_time(' '.join(str(result.find('p', "fecha").text).split(' ')[1:]).capitalize())
            symbol = str(result.find('p', "cambio-por").text)[0] if not str(result.find('p', "cambio-por").text)[0] == ' ' else ''
            color  = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
            percent = str(result.find('p', "cambio-por").text)[1:].strip()
            change = str(result.find('p', "cambio-num").text)

            data = InformationDollar(
                title=name,
                price=price,
                last_update=last_update,
                percent=percent,
                change=change,
                color=color,
                symbol=symbol
            )

            self.data[_convert_specific_format(name)] = asdict(data)

    def get_value_monitors(self, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        """
        El parámetro `monitor_code` indica el código del monitor del cual se desea obtener información, \
        mientras que el parámetro `prettify` permite mostrar los precios en formato de moneda con el símbolo de Bolívares. \
        Si se proporciona un nombre de propiedad válido, se devolverá el valor correspondiente para ese monitor.
        """
        self._scraped()

        if not monitor_code:
            return self.data
        
        try:
            monitor_data = self.data[monitor_code.lower()]
            if name_property:
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")
    
    def currency_converter(self, monitor_code: str, value, currency: str, prettify: bool = False):
        """
        Convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.

        monitor_code (str): El código del monitor a utilizar para la conversión.
        value (float or int): La cantidad de dinero a convertir.
        currency (str): La moneda en la que se encuentra la cantidad de dinero. Debe ser 'USD' o 'VES'.
        prettify (bool): Si es True, devuelve el resultado en un formato más legible. Por defecto es False (Bs. [VALUE] | $[VALUE]).
        """
        self._scraped()

        try:
            monitor_data = self.data[monitor_code]
            calculator = currency_converter(currency, value, monitor_data)
            
            if prettify and currency == 'VES':
                return f"${calculator}"
            elif prettify and currency == 'USD':
                return f"Bs. {calculator}"
            return f"{calculator}"
        except KeyError:
            raise KeyError("The monitor is invalid")