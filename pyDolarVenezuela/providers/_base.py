from typing import Any, Dict, List

class Base:
    PAGE = None
    
    @classmethod
    def _load(cls, **kwargs) -> List[Dict[str, Any]]:
        raise NotImplementedError
    
    @classmethod
    def get_values(cls, **kwargs) -> List[Dict[str, Any]]:
        try:
            result = cls._load(**kwargs)
            if not len(result) > 0:
                raise Exception(f'({cls.PAGE.name}) - Monitores no encontrados')
            return result
        except Exception as e:
            raise e