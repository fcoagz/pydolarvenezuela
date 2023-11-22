from dataclasses import dataclass

@dataclass
class Monitor:
    name: str
    provider: str
    currencies: list

BCV = Monitor(
    name="Banco Central de Venezuela",
    provider="http://www.bcv.org.ve/",
    currencies=['usd', 'eur', 'cny', 'try', 'rub']
)

CriptoDolar = Monitor(
    name="Cripto Dolar",
    provider="https://exchange.vcoud.com/",
    currencies=['usd', 'eur']
)

ExchangeMonitor = Monitor(
    name="Exchange Monitor",
    provider="https://exchangemonitor.net/",
    currencies=['usd', 'eur']
)

iVenezuela = Monitor(
    name="iVenezuela",
    provider="https://www.ivenezuela.travel/",
    currencies=['usd']
)

Dpedidos = Monitor(
    name="Monitor Dolar Venezuela",
    provider="https://api.lyldesarrollo.com/",
    currencies=['usd']
)