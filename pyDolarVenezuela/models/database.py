from dataclasses import dataclass

@dataclass
class Redis:
    """
    Redis instance
    """
    host: str = 'localhost'
    port: int = 6379
    password: str = None
    ttl: int = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(host={self.host!r}, port={self.port!r}, password={self.password!r}, ttl={self.ttl!r})'
