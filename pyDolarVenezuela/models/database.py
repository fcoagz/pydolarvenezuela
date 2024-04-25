from dataclasses import dataclass

@dataclass
class Redis:
    host: str = 'localhost'
    port: int = 6379
    password: str = None
    ttl: int = None