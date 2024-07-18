from .models import Page

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

DolarToday = Page(
    name="Dolar Today",
    provider="https://dolartoday.com/",
    currencies=['usd']
)

EnParaleloVzla = Page(
    name="EnParaleloVzla",
    provider="https://t.me/s/EnParaleloVzlatelegram",
    currencies=['usd']
)