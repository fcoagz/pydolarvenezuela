from typing import Any
import redis
from ..models.database import Redis

class Cache:
    def __init__(self, db: Redis) -> None:
        if not isinstance(db, Redis):
            raise TypeError("The parameter must be an object of type Redis.")
        
        self.r = redis.Redis(db.host, db.port, password=db.password, decode_responses=True)
    
    def set_data(self, key: str, value: Any, ttl: int = None):
        self.r.set(key, value)
        
        if ttl is not None:
            self.r.expire(key, ttl)
    
    def get_data(self, key: str) -> Any:
        return self.r.get(key)