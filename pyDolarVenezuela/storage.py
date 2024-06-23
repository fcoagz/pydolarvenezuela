from typing import Any, Union
from datetime import timedelta
from cachetools import TTLCache

class Cache:
    def __init__(self, maxsize: int = 1024, ttl: Union[int, timedelta] = timedelta(minutes=10)) -> None:
        """
        Inicializa el objeto Caché.

        Args:
        - maxsize: Total de items para almacenar
        - ttl: Tiempo de vida
        """
        self.ttl = ttl if isinstance(ttl, int) else ttl.seconds
        self.cache = TTLCache(maxsize=maxsize, ttl=self.ttl)
    
    def get(self, key: str):
        """
        Recupera un valor de la caché si existe y no ha caducado.

        Args:
        - key: Clave para llamar el valor
        """
        return self.cache.get(key)

    def set(self, key: str, value: Any):
        """
        Almacena un par clave-valor en la caché.

        Args:
        - key: Clave para llamar luego el valor guardado
        - value: Objeto
        """
        self.cache[key] = value