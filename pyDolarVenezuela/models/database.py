from typing import Optional
from dataclasses import dataclass

@dataclass 
class Database:
    """
    Database instance
    """
    motor: str
    host: str
    database: str
    port: str
    user: str
    password: str

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(host={self.host!r}, database={self.database!r}, port={self.port!r}, user={self.user!r}, password={self.password!r})'
    
@dataclass
class LocalDatabase:
    """
    Local database instance
    """
    motor: Optional[str] = 'sqlite'
    url: Optional[str] = 'database.db'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(database={self.database!r}, url={self.url!r})'