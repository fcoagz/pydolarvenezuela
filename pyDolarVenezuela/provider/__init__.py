from pyDolarVenezuela.pages import Monitor

from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela
from .dpedidos import Dpedidos

class Provider:
    @classmethod
    def select_monitor(self, monitor: Monitor, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        page = monitor.name

        if page == 'Banco Central de Venezuela':
            return BCV(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'Exchange Monitor':
            return ExchangeMonitor(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'Cripto Dolar':
            return CriptoDolar(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'iVenezuela':
            return iVenezuela(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'Monitor Dolar Venezuela':
            return Dpedidos(monitor.provider).get_values(monitor_code, name_property, prettify)