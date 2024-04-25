from dataclasses import dataclass

@dataclass
class Monitor:
    name: str
    provider: str
    currencies: list