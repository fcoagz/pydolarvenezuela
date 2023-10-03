from dataclasses import dataclass

@dataclass
class Monitor:
    name: str
    provider: str

BCV = Monitor(
    name="Banco Central de Venezuela",
    provider="http://www.bcv.org.ve/"
)

CriptoDolar = Monitor(
    name="Cripto Dolar",
    provider="https://exchange.vcoud.com/"
)

ExchangeMonitor = Monitor(
    name="Exchange Monitor",
    provider="https://exchangemonitor.net/"
)

iVenezuela = Monitor(
    name="iVenezuela",
    provider="https://www.ivenezuela.travel/"
)

Dpedidos = Monitor(
    name="Monitor Dolar Venezuela",
    provider="https://api.lyldesarrollo.com/"
)