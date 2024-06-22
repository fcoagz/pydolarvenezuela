![Portada pyDolarVenezuela](https://github.com/fcoagz/pydolarvenezuela/blob/main/static/pyDolarVenezuela.jpg?raw=true)

pyDolarVenezuela es una librería de Python diseñada para facilitar la obtención de los valores del dólar en distintos monitores en Venezuela. Esta herramienta te permite acceder a información actualizada proveniente de diversas páginas web que publican el valor del dólar en tiempo real:

| Página Web | URL | Estado
|------------|-------------|-------------|
| Exchange Monitor | https://exchangemonitor.net/dolar-venezuela | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| CriptoDolar | https://criptodolar.net/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| BCV (Banco Central de Venezuela) | http://www.bcv.org.ve/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| Italcambio | https://www.italcambio.com/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |
| Al Cambio | https://alcambio.app/ | ![Active](https://img.shields.io/badge/Activo-brightgreen) |

pyDolarVenezuela tiene como objetivo principal brindar una solución eficiente y confiable para acceder a información relevante sobre el valor del dólar en Venezuela, ofreciendo así una herramienta valiosa para desarrolladores interesados en trabajar en este ámbito.

## Base de datos

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

## Actividad

![Alt](https://repobeats.axiom.co/api/embed/4ee3c595fcdb3081e280a1e8f4f81af9767a37f7.svg "Repobeats analytics image")

## Instalación

``` sh
pip install pyDolarVenezuela
```

## Uso

Debes importar el módulo `pages`, donde encontrarás una variedad de atributos que contienen información sobre una página específica de la que deseas obtener los datos. Adicionalmente deberás importar la clase `Monitor`, cuyos parámetros será la página que deseas utilizar y la moneda en la que se expresarán los precios (`USD`, `EUR`).

```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
from pyDolarVenezuela import Monitor

monitor = Monitor(ExchangeMonitor, 'USD')
```

Si deseas utilizar una base de datos (lo cual es útil para calcular el cambio, el porcentaje, el color y el símbolo, y se devuelven los datos actualizados):


```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
from pyDolarVenezuela import Monitor, LocalDatabase

local = LocalDatabase(
    motor='sqlite',
    url='database.db'
)

monitor = Monitor(CriptoDolar, 'USD', db=local)

```

El parámetro `currency` de la clase `Monitor` por defecto tiene el valor: `USD`, verifique que la página de la que desea obtener los datos pueda expresar precios en `EUR`.

```python
print(ExchangeMonitor.currencies)

>> ['usd', 'eur']
```

El método `get_value_monitors` se utiliza después de crear una instancia del objeto Monitor y permite el acceso a los datos almacenados en el diccionario. Los siguientes parámetros serían los siguientes:

- `type_monitor`: El código del monitor del cual se desea obtener información. Por defecto es `None`.
- `property`: El nombre de la propiedad específica del diccionario de la información del monitor extraído que se desea obtener. Por defecto es `None`.
- `prettify`: Muestra los precios en formato de moneda con el símbolo de Bolívares. Por defecto es `False`.

```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
from pyDolarVenezuela import Monitor

monitor = Monitor(ExchangeMonitor, 'USD')

# Obtener los valores de todos los monitores
valores_dolar = monitor.get_all_monitors()

# Obtener el valor del dólar en EnParaleloVzla
valor_dolar = monitor.get_value_monitors("enparalelovzla", "price", prettify=True)

print(valor_dolar)
```

La función `currency_converter` convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.

```python
from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
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

## Contributores

<a href="https://github.com/fcoagz/pydolarvenezuela/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fcoagz/pydolarvenezuela"/>
</a>