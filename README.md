# pyDolarVenezuela
pyDolarVenezuela es una librería de Python que te permite obtener los valores del dólar en diferentes monitores en Venezuela, así como las tasas de cambio del Banco Central de Venezuela. Con esta librería, puedes acceder a los precios del dólar en monitores como EnParaleloVzla, MonitorDolarWeb y Binance, y obtener información actualizada de las tasas de cambio para las monedas EUR, CNY, TRY y USD. La librería es fácil de usar y ofrece una manera rápida y eficiente de obtener información relevante sobre el mercado cambiario en Venezuela.

## Instalación
``` sh
pip install pyDolarVenezuela
```

## Uso
La clase `Monitor` de la librería pyDolarVenezuela te permite obtener los valores del dólar en diferentes monitores en Venezuela.

La clase tiene dos métodos principales:

`_load()`: Este método se encarga de cargar los datos de los monitores a través del scraping de la página web de referencia y almacenarlos en un diccionario.

`get_value_monitors()`: Este método permite acceder a los datos almacenados en el diccionario. El parámetro `monitor_code` indica el código del monitor del cual se desea obtener información, `name_property` accedes a la propiedad del diccionario para obtener su valor, mientras que el parámetro `prettify` permite mostrar los precios en formato de moneda con el símbolo de Bolívares. Si se proporciona un nombre de propiedad válido, se devolverá el valor correspondiente para ese monitor.

### Ejemplo
``` py
import pyDolarVenezuela as pdv

monitor = pdv.Monitor()

# Obtener los valores de todos los monitores
values = monitor.get_value_monitors()

# Obtener el valor del dólar en EnParaleloVzla
get_value_enparalelovzla = monitor.get_value_monitors(monitor_code=2, name_property='price', prettify=True)

# Obtener la ultima actualizacion del dólar en Binance
get_value_binance = monitor.get_value_monitors(monitor_code=17, name_property='last_update' prettify=False)
```

La clase `Bcv` tiene el siguiente metodo:

- `Bcv().get_rates()`: Te muestra los valores de las tasas de cambio del Banco Central de Venezuela. EUR, CNY, TRY, USD.

Los parametros del metodo ante mencionado son los siguientes:

- `currency_code`: Acepta un código de moneda o fecha como argumento.
- `prettify`: Acepta un valor booleano si desea que el valor de la moneda salga junto con el simbolo de Bolivares. `Bs. [VALOR]`.

### Ejemplo
``` py
import pyDolarVenezuela as pdv

bcv = pdv.Bcv()

get_value_usd = bcv.get_rates(currency_code='USD', prettify=True)
get_value_eur = bcv.get_rates(currency_code='EUR', prettify=False)
```