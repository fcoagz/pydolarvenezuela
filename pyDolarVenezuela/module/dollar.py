from dataclasses import dataclass

@dataclass
class InformationDollar:
    title: str
    price: str
    last_update: str
    percent: str
    change: str
    color: str
    symbol: str