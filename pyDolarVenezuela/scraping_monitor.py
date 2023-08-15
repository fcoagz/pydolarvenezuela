from bs4 import BeautifulSoup

from pyDolarVenezuela.request import get_content_page
from pyDolarVenezuela.util import PAGINA_PRINCIPAL_EXCHANGE_MONITOR

def _get_values_monitors(soup: BeautifulSoup):
    return [value for value in soup]

def _get_date_value(soup: BeautifulSoup):
    return str(soup.find('p')).split("<br/>")[-1].replace("</p>", "")

def _convert_specific_format(text: str) -> str:
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', '_')
    return text

class Monitor(object):
    """
    La clase Monitor permite consultar los precios del dólar en diversos monitores en Venezuela. \n
    El método `_load` carga los datos de los monitores a través del scraping de la página web de referencia, donde los datos son almacenados en un diccionario. \ 
    El método `get_value_monitors` permite acceder a los datos almacenados en el diccionario.
    """
    def _load(self):
        soup = BeautifulSoup(get_content_page(PAGINA_PRINCIPAL_EXCHANGE_MONITOR), "html.parser")
        section_dolar_venezuela = soup.find_all("div", "col-xs-12 col-sm-6 col-md-4 col-tabla")
        section_fecha_valor = soup.find("div", "col-xs-12 text-center")

        date = _get_date_value(section_fecha_valor)
        all_monitors = _get_values_monitors(section_dolar_venezuela)

        self.all_monitors = {}
        self.all_monitors['value'] = {"date": date}
        i: int = 0
        for monitor in all_monitors:
            monitor = monitor.find("div", "module-table module-table-fecha")
            change = str(monitor.find('p', 'cambio-por').text)
            text_price = str(monitor.find('p', 'precio').text).replace(',', '.')

            data = {
                "title": monitor.find('h6', 'nombre').text,
                "price": text_price.replace('.', '', 1) if text_price.count('.') == 2 else text_price,
                "change": ("\U00002B07" + change[1:] if change[0] == '▼' else "\U00002B06" + change[1:] if change[0] == '▲' else "" + change[1:]),
                "last_update": ' '.join(str(monitor.find('p', 'fecha').text).split(' ')[1:])
            }
            self.all_monitors[_convert_specific_format(data['title'])] = data
            
    
    def get_value_monitors(self, monitor_code: str = None, name_property: str = None, prettify: bool = False):
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