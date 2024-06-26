from .models.pages import Page

BCV = Page(
    name="Banco Central de Venezuela",
    provider="http://www.bcv.org.ve/",
    currencies=['usd']
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

Italcambio = Page(
    name="Italcambio",
    provider="https://www.italcambio.com/index.php",
    currencies=['usd']
)

AlCambio = Page(
    name="Al Cambio",
    provider="https://api.alcambio.app/graphql",
    currencies=['usd']
)