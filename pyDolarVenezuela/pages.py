from .models.pages import Page

BCV = Page(
    name="Banco Central de Venezuela",
    provider="http://www.bcv.org.ve/",
    currencies=['usd', 'eur', 'cny', 'try', 'rub']
)

CriptoDolar = Page(
    name="Cripto Dolar",
    provider="https://exchange.vcoud.com/",
    currencies=['usd', 'eur']
)

ExchangeMonitor = Page(
    name="Exchange Monitor",
    provider="https://exchangemonitor.net/",
    currencies=['usd', 'eur']
)