from typing import List, Type

from ._base import Base
from .alcambio import AlCambio
from .bcv import BCV
from .criptodolar import CriptoDolar
from .dolartoday import DolarToday
from .exchangemonitor import ExchangeMonitor
from .enparalelovzla import EnParaleloVzla
from .italcambio import Italcambio

providers: List[Type[Base]] = [AlCambio, BCV, CriptoDolar, DolarToday, ExchangeMonitor, EnParaleloVzla, Italcambio]