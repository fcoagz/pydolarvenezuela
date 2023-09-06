from pyBCV import Currency
from decimal import Decimal

class Bcv:
    def get_rates(self, currency_code: str, prettify: bool = True):
        round_number_rate = Decimal(Currency().get_rate(currency_code=currency_code, prettify=False))
        round_number_rate = round(round_number_rate, 2)
        return round_number_rate if not prettify else f"Bs. {round_number_rate:,.2f}"