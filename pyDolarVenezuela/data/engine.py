from typing import Union
from sqlalchemy import create_engine
from .models import Base
from ..models import Database, LocalDatabase

# https://github.com/orgs/supabase/discussions/27071 Using SQLAlchemy with Supabase
def get_connection(connection: Union[Database, LocalDatabase]):
    """
    Obtiene un motor de base de datos (engine) de SQLAlchemy según el tipo de conexión proporcionada.
    """
    if isinstance(connection, Database):
        return create_engine(f'{connection.motor}://{connection.user}:{connection.password}@{connection.host}:{connection.port}/{connection.database}')
    elif isinstance(connection, LocalDatabase):
        return create_engine(f'{connection.motor}:///{connection.url}')

def create_tables(engine):
    """
    Crea todas las tablas definidas en los modelos utilizando el motor de base de datos proporcionado.
    """
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        raise e