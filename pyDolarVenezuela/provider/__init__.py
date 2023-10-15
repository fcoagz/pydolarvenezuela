from pyDolarVenezuela.pages import Monitor
from pyDolarVenezuela.pages import ( BCV as B, CriptoDolar as C, ExchangeMonitor as E, iVenezuela as I, Dpedidos as D )

from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela
from .dpedidos import Dpedidos

class Provider:
    @classmethod
    def select_monitor(self, monitor: Monitor, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        if monitor.name == B.name:
            return BCV(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif monitor.name == C.name:
            return CriptoDolar(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif monitor.name == E.name:
            return ExchangeMonitor(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif monitor.name == I.name:
            return iVenezuela(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif monitor.name == D.name:
            return Dpedidos(monitor.provider).get_values(monitor_code, name_property, prettify)