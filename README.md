# pyDolarVenezuela
**pyDolarVenezuela** es una libreria de Python que permite obtener los valores de diferentes monitores del dolar en Venezuela y las tasas de cambio del Banco Central de Venezuela.

## Instalación
``` sh
pip install pyDolarVenezuela
```

## Uso
La clase `pyDolarVenezuela.Monitor` tiene el siguiente metodo:

- `Monitor().get_value_monitors()`: Te muestra los valores del dolar no oficial. EnParaleloVzla, MonitorDolarWeb, Binance.

Los parametros del metodo ante mencionado son los siguientes:

- `monitor_code`: Acepta el nombre de cada monitor que desea conocer su valor.
- `prettify`: Acepta un valor booleano si desea que el valor de la moneda salga junto con el simbolo de Bolivares. `Bs. [VALOR]`.

### Ejemplo
``` py
import pyDolarVenezuela as pdv

monitor = pdv.Monitor()

get_value_enparalelovzla = monitor.get_value_monitors(monitor_code='enparalelovzla', prettify=True)
get_value_binance = monitor.get_value_monitors(monitor_code='binance', prettify=False)
```

La clase `pyDolarVenezuela.Bcv` tiene el siguiente metodo:

- `Bcv().get_rate()`: Te muestra los valores de las tasas de cambio del Banco Central de Venezuela. EUR, CNY, TRY, USD.

Los parametros del metodo ante mencionado son los siguientes:

- `currency_code`: Acepta un código de moneda o fecha como argumento.
- `prettify`: Acepta un valor booleano si desea que el valor de la moneda salga junto con el simbolo de Bolivares. `Bs. [VALOR]`.

### Ejemplo
``` py
import pyDolarVenezuela as pdv

bcv = pdv.Bcv()

get_value_usd = bcv.get_rate(currency_code='USD', prettify=True)
get_value_eur = bcv.get_rate(currency_code='EUR', prettify=False)
```