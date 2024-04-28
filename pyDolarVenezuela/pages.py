from .models.pages import Monitor

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