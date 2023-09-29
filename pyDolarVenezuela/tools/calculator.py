def _bs_to_dollar(value: float, price_monitor: float):
    return value / price_monitor

def _dollar_to_bs(value: float, price_monitor: float):
    return value * price_monitor

def _isnumber(_object):
    if isinstance(_object, int) or isinstance(_object, float):
        return True
    return False

def currency_converter(type: str, value, monitor: dict):
    """
    Convierte una cantidad de dinero de una moneda a otra utilizando los datos de un monitor específico.
    """
    price_monitor = monitor['price']

    if _isnumber(value):
        if type == 'VES':
            return _bs_to_dollar(value, float(price_monitor))
        elif type == 'USD':
            return _dollar_to_bs(value, float(price_monitor))
        else:
            raise ValueError(f"The type must be USD or VES not {type}")
    else:
        raise TypeError(f"The value must be an integer or floating point number, not {value}")