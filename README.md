# pyDolarVenezuela
Esta es una libreria desarrollado en Python te permite consultar los precios del dólar en diferente monitores en Venezuela.

## Instalación
Para instalar esta librería, puedes utilizar el siguiente comando de pip:

```py
pip install pyDolarVenezuela
```
En Linux o Mac:
```py
pip3 install pyDolarVenezuela
```
## Uso
1. Importamos la librería:
```py
from pyDolarVenezuela import price
```
2. Para consultar la libreria, debemos crear una variable `precios` dentro de ella estara nuestra funcion `price()`:
```py
from pyDolarVenezuela import price

precios = price()
print(precios)

>> {
  '$bcv': 'Bs. 24.497',
  '$enparalelovzla': 'Bs. 25.11',
  '$dolartoday': 'Bs. 25.15',
  '$monitordolarweb': 'Bs. 25.02',
  '$enparalelovzlavip': 'Bs. 25.04',
  '$binancep2p': 'Bs. 25.020'
   }
```
Retorna una estructura en formato JSON.

3. Para acceder una de ellas se hace de la siguiente manera:
```py
from pyDolarVenezuela import price

precios = price()
print(precios['$bcv'])

>> Bs. 24.497
```
