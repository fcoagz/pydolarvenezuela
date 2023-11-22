![Portada pyDolarVenezuela](https://github.com/fcoagz/pydolarvenezuela/blob/main/static/pyDolarVenezuela.jpg?raw=true)

pyDolarVenezuela es una librería de Python que te brinda la posibilidad de obtener los valores del dólar en distintos monitores en Venezuela, así como las tasas de cambio proporcionadas por el Banco Central de Venezuela. Esta librería consulta diversas páginas web que ofrecen información actualizada sobre el valor del dólar:

| Página Web | URL | Estado
|------------|-------------|-------------|
| Exchange Monitor | https://exchangemonitor.net/dolar-venezuela | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| CriptoDolar | https://criptodolar.net/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| BCV (Banco Central de Venezuela) | http://www.bcv.org.ve/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| iVenezuela | https://www.ivenezuela.travel/ | ![Inactive](https://img.shields.io/badge/Inactivo-red) |
| Dpedidos | https://dpedidos.com/ | ![Inactive](https://img.shields.io/badge/Inactivo-red) |


pyDolarVenezuela tiene como objetivo principal brindar una solución eficiente y confiable para acceder a información relevante sobre el valor del dólar en Venezuela, ofreciendo así una herramienta valiosa para desarrolladores interesados en trabajar en este ámbito.

## Instalación
``` sh
pip install pyDolarVenezuela
```

## Uso
Debes importar el módulo `pages`, donde encontrarás una variedad de atributos que contienen información sobre una página específica de la que deseas obtener los datos. Adicionalmente deberás importar la clase `Monitor`, cuyos parámetros será la página que deseas utilizar y la moneda en la que se expresarán los precios (`USD`, `EUR`).

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor
from pyDolarVenezuela import Monitor

monitor = Monitor(ExchangeMonitor, 'USD')
```

El parámetro `currency` de la clase `Monitor` por defecto tiene el valor: `USD`, verifique que la página de la que desea obtener los datos pueda expresar precios en `EUR`.

```python
print(ExchangeMonitor.currencies)

>> ['usd', 'eur']
```
El método `get_value_monitors` se utiliza después de crear una instancia del objeto Monitor y permite el acceso a los datos almacenados en el diccionario. Los siguientes parámetros serían los siguientes:

- `monitor_code`: El código del monitor del cual se desea obtener información. Por defecto es `None`.
- `name_property`: El nombre de la propiedad específica del diccionario de la información del monitor extraído que se desea obtener. Por defecto es `None`.
- `prettify`: Muestra los precios en formato de moneda con el símbolo de Bolívares. Por defecto es `False`.

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor
from pyDolarVenezuela import Monitor

monitor = Monitor(ExchangeMonitor, 'USD')

# Obtener los valores de todos los monitores
valores_dolar = monitor.get_value_monitors()

# Obtener el valor del dólar en EnParaleloVzla
valor_dolar = monitor.get_value_monitors("enparalelovzla", "price", prettify=True)

print(valor_dolar)
```

La función `currency_converter` convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.

```python
from pyDolarVenezuela.pages import BCV, CriptoDolar, ExchangeMonitor
from pyDolarVenezuela import Monitor
from pyDolarVenezuela import currency_converter

monitor = Monitor(ExchangeMonitor, 'USD')

information_dolar = monitor.get_value_monitors("enparalelovzla")
price_in_dolares = currency_converter(
    type='VES', # VES | USD | EUR
    value=1000, # Bs. 1000
    monitor=information_dolar # Datos del dolar
)

print(price_in_dolares)  # Imprime algo como 28.22466836014677
```