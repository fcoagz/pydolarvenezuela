def _convert_specific_format(text: str, character: str = '_') -> str:
    """
    Formatea el nombre de moneda para omologar todas las salidas de los datos de un monitor específico.
    """
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acento, sin_acento in acentos.items():
        text = text.lower().replace(acento, sin_acento).replace(' ', character)
    return text

def _parse_price(price: str) -> float:
    """
    Convierte el formato de una moneda a de "," al uso del "." (Formato standard).
    """
    price = price.replace(',', '.')
    if price.count('.') == 2:
        price = price.replace('.', '', 1)
    return float(price)

def _parse_percent(percent: str) -> float:
    """
    Convierte el formato del cambio porcentual de "," al uso del "." y agrega el simbolo "%".
    """
    return float(percent.strip().replace(',', '.').replace('%', ''))

def _convert_dollar_name_to_monitor_name(monitor_name: str):
    """
    Cambiar el nombre de los monitores existentes a su nombre original. (Dolar Today, EnParaleloVzla)
    """
    if monitor_name.split(' ')[0] in ['Dólar', 'Euro'] and monitor_name not in ['Dólar Today', 'Euro Today']:
        if monitor_name == 'Dólar Paralelo':
            return 'DolarToday'
        if monitor_name in ['Dólar Monitor', 'Euro Monitor']:
            return 'EnParaleloVzla'
        else:
            return monitor_name.split(' ')[1]
    return monitor_name