from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela
from .dpedidos import Dpedidos

from ..pages import Monitor
from ..pages import BCV as B, CriptoDolar as C, Dpedidos as D, ExchangeMonitor as E, iVenezuela as I 

monitor_classes = {
    'usd': {
        B.name: BCV,
        C.name: CriptoDolar,
        E.name: ExchangeMonitor,
        D.name: Dpedidos,
        I.name: iVenezuela
    },
    'eur': {
        B.name: BCV,
        C.name: CriptoDolar,
        E.name: ExchangeMonitor
    }
}

def select_monitor(provider: Monitor, **kwargs):
    currency = kwargs.get('currency')
    monitor_code = kwargs.get('monitor_code')
    name_property = kwargs.get('name_property')
    prettify = kwargs.get('prettify', False)

    if currency not in ['usd', 'eur']:
        raise ValueError(f"The currency type must be 'usd' or 'eur', not {currency}")

    try:
        monitor_class = monitor_classes.get(currency).get(provider.name)
        if monitor_class is not None:
            return monitor_class(provider.provider, currency).get_values(
                monitor_code=monitor_code,
                name_property=name_property, 
                prettify=prettify
            )
        else:
            raise ValueError("Provider not supported")
    except Exception as e:
        raise e