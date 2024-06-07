from typing import Any
import redis
from ..models.database import Redis

class Cache:
    def __init__(self, db: Redis) -> None:
        """
        Gestionar la interacción con una base de datos Redis.
        """
        if not isinstance(db, Redis):
            raise TypeError("The parameter must be an object of type Redis.")
        self._connect_to_redis(db)

    def _connect_to_redis(self, db: Redis):
        """
        Establece la conexión con la base de datos Redis.
        """
        try:
            self.r = redis.Redis(host=db.host, port=db.port, password=db.password, decode_responses=True)
        
        except redis.ConnectionError as e:
            raise ConnectionError(f"Could not connect to Redis: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")
    
    def set_data(self, key: str, value: Any, ttl: int = None):
        """
        Establezca el valor en el nombre de la clave en valor.

        Con `ttl`. Puede establecer un límite de tiempo durante el cual se guardarán los datos.
        """
        self.r.set(key, value)
        
        if ttl is not None:
            self.r.expire(key, ttl)
    
    def delete_data(self, key: str):
        """
        Elimina los datos argumentando la clave que estableciste en ese valor.
        """
        self.r.delete(key)
    
    def get_data(self, key: str) -> Any:
        """
        Obtener los datos
        """
        return self.r.get(key)