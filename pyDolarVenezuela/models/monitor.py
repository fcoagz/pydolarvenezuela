from typing import Optional
from dataclasses import dataclass

@dataclass
class Monitor:
    """
    MonitorDB instance
    """
    key: str
    title: str  
    price: float  
    price_old: Optional[float] = None 
    last_update: Optional[str] = None  
    image: Optional[str] = None  
    percent: Optional[float] = 0.0
    change: Optional[float] = 0.0  
    color: Optional[str] = "neutral" 
    symbol: Optional[str] = "" 

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title}, price={self.price}, price_old={self.price_old}, last_update={self.last_update}, percent={self.percent}, change={self.change}, color={self.color}, symbol={self.symbol}, image={self.image})"