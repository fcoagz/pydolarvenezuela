from typing import Literal, Union
from ..models import Monitor

def currency_converter(type: Literal['VES', 'USD', 'EUR'], value, monitor: Union[Monitor, dict]) -> Union[float, None]:
    """
    Convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.
    """
    price_monitor = monitor.price if isinstance(monitor, Monitor) else monitor.get('price', None)
    if not price_monitor:
        raise KeyError('The monitor was not found')

    try:
        if isinstance(value, int) or isinstance(value, float):
            if type == 'VES':
                return value / float(price_monitor)
            elif type in ['USD', 'EUR']:
                return value * float(price_monitor)
            else:
                raise ValueError(f"The type must be USD or VES not {type}")
    except TypeError as e:
        raise e