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

Italcambio = Page(
    name="Italcambio",
    provider="https://www.italcambio.com/index.php",
    currencies=['usd', 'dkk', 'cop', 'nok', 'gbp', 'sek', 'clp', 'chf', 'hkd', 'twd', 'brl', 'cad', 'eur', 'bob', 'nio', 'ars', 'cny', 'ils', 'jpy', 'pen', 'dop', 'ttd', 'uyu', 'ang', 'aud']
)