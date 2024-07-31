![Portada pyDolarVenezuela](https://github.com/fcoagz/pydolarvenezuela/blob/main/static/pyDolarVenezuela.jpg?raw=true)

pyDolarVenezuela es una librería de Python diseñada para facilitar la obtención de los valores del dólar en distintos monitores en Venezuela. Esta herramienta te permite acceder a información actualizada proveniente de diversas páginas web que publican el valor del dólar en tiempo real:

| Página Web | URL | Estado
|------------|-------------|-------------|
| Exchange Monitor | https://exchangemonitor.net/dolar-venezuela | ![Pending](https://img.shields.io/badge/Pendiente-orange) |
| CriptoDolar | https://criptodolar.net/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| BCV (Banco Central de Venezuela) | http://www.bcv.org.ve/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| Italcambio | https://www.italcambio.com/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| Al Cambio | https://alcambio.app/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| DolarToday | https://dolartoday.com/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| EnParaleloVzla | https://t.me/enparalelovzlatelegram | ![Active](https://img.shields.io/badge/Activo-brightgreen) |

pyDolarVenezuela tiene como objetivo principal brindar una solución eficiente y confiable para acceder a información relevante sobre el valor del dólar en Venezuela, ofreciendo así una herramienta valiosa para desarrolladores interesados en trabajar en este ámbito.

## Características

### Base de datos

[![Made with Supabase](https://supabase.com/badge-made-with-supabase-dark.svg)](https://supabase.com)

pyDolarVenezuela utiliza [Supabase](https://supabase.com) para la integración de la base de datos Postgres. También puede implementar otro servidor de base de datos si lo prefiere o localmente.

```python
from pyDolarVenezuela import LocalDatabase, Database

local = LocalDatabase(
    motor='sqlite',
    url='database.db' # Ubicación de la base de datos
)

db_server = Database(
    motor='postgresql',
    host='postgres-cloud-host',
    port='postgres-cloud-port',
    user='postgres-cloud-user',
    password='your-secure-password',
    database='postgres-cloud-database-name'
)
```

**Nota:** Se pueda utilizar con SQLAlchemy.

### Almacenamiento en caché

Proporciona almacenamiento en caché integrado para una rápida recuperación de datos para mejorar el rendimiento al realizar solicitudes a la misma fuente. Puedes configurar el tiempo de espera si lo deseas.

```python
from datetime import timedelta
from pyDolarVenezuela import Monitor

monitor = Monitor(..., ttl=timedelta(minutes=5))
```

## Actividad

![Alt](https://repobeats.axiom.co/api/embed/4ee3c595fcdb3081e280a1e8f4f81af9767a37f7.svg "Repobeats analytics image")

## Instalación

``` sh
pip install pyDolarVenezuela
```

## Uso

### Importación de las páginas

El módulo `pages`, encontrarás una variedad de atributos que contienen información sobre una página específica de la que deseas obtener los datos. Adicionalmente deberás importar la clase `Monitor`, cuyos parámetros será la página que deseas utilizar, la moneda en la que se expresarán los precios (`USD`, `EUR`) y entre otras.

```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, DolarToday, ExchangeMonitor, EnParaleloVzla, Italcambio
from pyDolarVenezuela import Monitor

monitor = Monitor(AlCambio, 'USD')
```

Como se mencionó anteriormente, puede utilizar una base de datos (que es útil para calcular cambios, porcentajes, colores y símbolos).

El parámetro `currency` de la clase `Monitor` por defecto tiene el valor: `USD`, verifique que la página de la que desea obtener los datos pueda expresar precios en `EUR`.

```python
print(AlCambio.currencies)

>> ['usd']
```

### Métodos disponibles

#### `get_all_monitors`

Se utiliza para obtener todos los datos de los monitores que se encuentran en dicha página.

#### `get_value_monitors`

Se utiliza para obtener datos de un monitor específico y acceder a ellos fácilmente.

Argumentos:

- `type_monitor`: El código del monitor del cual se desea obtener información.
- `property`: El nombre de la propiedad específica del diccionario de la información del monitor extraído que se desea obtener. Por defecto es `None`.
- `prettify`: Muestra los precios en formato de moneda con el símbolo de Bolívares. Por defecto es `False`.

#### `get_prices_history`

Le permite obtener el historial de precios de cierre de un monitor específico.

Argumentos:

- `type_monitor`: El código del monitor del cual se desea obtener información.
- `start_date`: Fecha de inicio del historial.
- `end_date`: Fecha de fin del historial. Por defecto es la fecha actual.

#### `get_daily_price_monitor`

Le permite obtener todos los cambios realizados en un día para un monitor específico.

Argumentos:

- `type_monitor`: El código del monitor del cual se desea obtener información.
- `date`: Fecha de la cual se desea obtener los precios.

**Nota**: Para `get_prices_history` y `get_daily_price_monitor`. Debe establecer una base de datos y puede utilizarla siempre que mantenga el script activo y alimente la base de datos.

#### `currency_converter`

Convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.

Argumentos:

- `type`: Tipo de conversión. (VES, USD, EUR)
- `value`: Monto a convertir.
- `monitor`: La data del monitor una vez obtenido sus datos.

### Código de ejemplo

```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, DolarToday, ExchangeMonitor, EnParaleloVzla, Italcambio
from pyDolarVenezuela import Monitor, Database

db = Database(...)
monitor = Monitor(AlCambio, 'USD', db=db)

# Obtener los valores de todos los monitores
all_monitors = monitor.get_all_monitors()

# Obtener el valor del dólar en EnParaleloVzla
paralelo_value = monitor.get_value_monitors("enparalelovzla", "price", prettify=True)

# Obtener el historial de precios de un monitor durante una semana.
history = monitor.get_prices_history("enparalelovzla", "01-07-2024", "05-07-2024")

# Obtener todos los cambios que se realizaron de un monitor.
changes = monitor.get_daily_price_monitor("enparalelovzla", "30-07-2024")

# Conversion
data_paralelo = monitor.get_value_monitors("enparalelovzla")
price_in_dolares = currency_converter(
    type='VES', # VES | USD | EUR
    value=1000, # Bs. 1000
    monitor=information_dolar # Datos del dolar
)
```

### Configuración de fecha

Respetando el tipado de las fechas. Te muestro cómo puedes formatearlo.

```python
from datetime import datetime
from pyDolarVenezuela.pages import AlCambio
from pyDolarVenezuela import Monitor

monitor = Monitor(AlCambio, 'USD')

paralelo    = monitor.get_value_monitors("enparalelovzla")
last_update = datetime.strftime(paralelo['last_update'], '%d-%m-%Y %H:%M:%S')

print(last_update)
```
Para que puedas mostrar la fecha como desees.

## Contributores

<a href="https://github.com/fcoagz/pydolarvenezuela/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fcoagz/pydolarvenezuela"/>
</a>