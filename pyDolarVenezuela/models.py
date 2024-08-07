from typing import Optional
from datetime import datetime
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
        return f'{self.__class__.__name__}(motor={self.motor!r}, url={self.url!r})'

@dataclass
class Page:
    """
    Page instance
    """
    name: str
    provider: str
    currencies: list

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, provider={self.provider!r}, currencies={self.currencies!r})'
    
@dataclass
class Monitor:
    """
    Monitor instance
    """
    key: str
    title: str  
    price: float  
    price_old: Optional[float] = None 
    last_update: Optional[datetime] = None  
    image: Optional[str] = None  
    percent: Optional[float] = 0.0
    change: Optional[float] = 0.0  
    color: Optional[str] = "neutral" 
    symbol: Optional[str] = "" 

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r}, price={self.price!r}, price_old={self.price_old!r}, last_update={self.last_update!r}, percent={self.percent!r}, change={self.change!r}, color={self.color!r}, symbol={self.symbol!r}, image={self.image!r})"
    
@dataclass
class HistoryPrice:
    """
    History price instance
    """
    price: float
    last_update: datetime

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(price={self.price!r}, last_update={self.last_update!r})'

@dataclass
class Image:
    """
    Image instance
    """
    title: str
    image: str
    provider: str

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(title={self.title!r}, provider={self.provider!r}, image={self.image!r})'