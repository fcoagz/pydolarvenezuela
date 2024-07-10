from typing import Any, Dict, List, Union

class Base:
    PAGE = None
    
    @classmethod
    def _load(cls, **kwargs) -> List[Union[Dict[str, Any], None]]:
        raise NotImplementedError
    
    @classmethod
    def get_values(cls, **kwargs) -> List[Union[Dict[str, Any], None]]:
        result = cls._load(**kwargs)
        return result