from pyDolarVenezuela.pages import Monitor

from .bcv import BCV
from .criptodolar import CriptoDolar
from .exchangemonitor import ExchangeMonitor
from .ivenezuela import iVenezuela

from urllib.parse import urlparse

def get_name_the_page(url: str):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')

    if len(domain_parts) == 2:
        return domain_parts[0]
    else:
        main_domain = domain_parts[-3] if not domain_parts[-3] == 'www' else domain_parts[-2]
    
    return main_domain

class Provider:
    @classmethod
    def select_monitor(self, monitor: Monitor, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        page = get_name_the_page(monitor.provider)

        if page == 'bcv':
            return BCV(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'exchangemonitor':
            return ExchangeMonitor(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'exchange':
            return CriptoDolar(monitor.provider).get_values(monitor_code, name_property, prettify)
        elif page == 'ivenezuela':
            return iVenezuela(monitor.provider).get_values(monitor_code, name_property, prettify)