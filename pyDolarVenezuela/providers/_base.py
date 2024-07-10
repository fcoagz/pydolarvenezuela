from typing import Any, Dict, List, Union

class Base:
    PAGE = None
    
    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        raise NotImplementedError
    
    @classmethod
    def get_values(cls, **kwargs) -> List[Dict[str, Any]]:
        result = cls._load(**kwargs)
        return result