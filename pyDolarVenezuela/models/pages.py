from dataclasses import dataclass

@dataclass
class Monitor:
    """
    Monitor instance
    """
    name: str
    provider: str
    currencies: list

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, provider={self.provider!r}, currencies={self.currencies!r})'