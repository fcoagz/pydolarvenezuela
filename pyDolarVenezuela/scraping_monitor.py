from bs4 import BeautifulSoup

from pyDolarVenezuela.request import get_content_page
from pyDolarVenezuela.util import PAGINA_PRINCIPAL_EXCHANGE_MONITOR

def _get_values_monitors(soup: BeautifulSoup):
    return [value for value in soup]

class Monitor(object):
    """
    La clase Monitor permite consultar los precios del dólar en diversos monitores en Venezuela. \n
    El método `_load` carga los datos de los monitores a través del scraping de la página web de referencia, donde los datos son almacenados en un diccionario. \ 
    El método `get_value_monitors` permite acceder a los datos almacenados en el diccionario.
    """
    def _load(self):
        soup = BeautifulSoup(get_content_page(PAGINA_PRINCIPAL_EXCHANGE_MONITOR), "html.parser")
        section_dolar_venezuela = soup.find_all("div", "col-xs-12 col-sm-6 col-md-4 col-tabla")
        all_monitors = _get_values_monitors(section_dolar_venezuela)

        self.all_monitors = {}
        i: int = 0
        for monitor in all_monitors:
            monitor = monitor.find("div", "module-table module-table-fecha")
            data = {
                "name": monitor.find('h6', 'nombre').text,
                "unit": monitor.find('p', 'unidad').text,
                "price": str(monitor.find('p', 'precio').text).replace(',', '.'),
                "last_update": monitor.find('p', 'fecha').text
            }
            self.all_monitors[i] = data
            i += 1
    
    def get_value_monitors(self, monitor_code: int = None, name_property: str = None, prettify: bool = False):
        """
        El parámetro `monitor_code` indica el código del monitor del cual se desea obtener información, \
        mientras que el parámetro `prettify` permite mostrar los precios en formato de moneda con el símbolo de Bolívares. \
        Si se proporciona un nombre de propiedad válido, se devolverá el valor correspondiente para ese monitor.
        """
        self._load()

        if not monitor_code:
            return self.all_monitors
        if monitor_code not in self.all_monitors:
            raise ValueError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")
        
        return (f"Bs. {self.all_monitors[monitor_code][name_property]}" if prettify and name_property == "price"
                else self.all_monitors[monitor_code][name_property] if name_property in self.all_monitors[monitor_code]
                else self.all_monitors[monitor_code])