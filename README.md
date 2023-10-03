# pyDolarVenezuela
pyDolarVenezuela es una librería de Python que te brinda la posibilidad de obtener los valores del dólar en distintos monitores en Venezuela, así como las tasas de cambio proporcionadas por el Banco Central de Venezuela. Esta librería consulta diversas páginas web que ofrecen información actualizada sobre el valor del dólar:

| Página Web | URL | Estado
|------------|-------------|-------------|
| Exchange Monitor | https://exchangemonitor.net/dolar-venezuela | OK |
| CriptoDolar | https://criptodolar.net/ | OK |
| BCV (Banco Central de Venezuela) | http://www.bcv.org.ve/ | OK |
| iVenezuela | https://www.ivenezuela.travel/ | OK |
| Dpedidos | https://dpedidos.com/ | TEST |


pyDolarVenezuela tiene como objetivo principal brindar una solución eficiente y confiable para acceder a información relevante sobre el valor del dólar en Venezuela, ofreciendo así una herramienta valiosa para desarrolladores interesados en trabajar en este ámbito.

## Instalación
``` sh
pip install pyDolarVenezuela
```

## Uso
Para utilizar la librería, debes importar el módulo `pages`, donde encontrarás las variables que contienen la información sobre la página de donde obtendrás los valores. Además, deberás importar la clase `Monitor`, cuyo parámetro será la página que deseas utilizar.

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor, iVenezuela, Dpedidos
from pyDolarVenezuela import Monitor

monitor = Monitor(CriptoDolar)
```
El método `get_value_monitors()` se utiliza después de crear una instancia del objeto Monitor y permite acceder a los datos almacenados en el diccionario. Utiliza los parámetros `monitor_code`, name_property y `prettify` para obtener valores específicos y mostrarlos en formato monetario con símbolo de Bolívares si es necesario.

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor, iVenezuela, Dpedidos
from pyDolarVenezuela import Monitor

monitor = Monitor(CriptoDolar)

# Obtener los valores de todos los monitores
valores_dolar = monitor.get_value_monitors()

# Obtener el valor del dólar en EnParaleloVzla
valor_dolar = monitor.get_value_monitors("enparalelovzla", "price", prettify=True)

print(valor_dolar)
```

La función `currency_converter` convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor, iVenezuela, Dpedidos
from pyDolarVenezuela import Monitor
from pyDolarVenezuela import currency_converter

monitor = Monitor(CriptoDolar)

information_dolar = monitor.get_value_monitors("enparalelovzla")
price_in_dolares = currency_converter(
    type='VES', # VES | USD
    value=1000, # Bs. 1000
    monitor=information_dolar # Datos del dolar
)

print(price_in_dolares)  # Imprime algo como 28.22466836014677
```