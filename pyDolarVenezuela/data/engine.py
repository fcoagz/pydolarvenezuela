from typing import Union
from sqlalchemy import create_engine
from .models import Base
from ..models import Database, LocalDatabase

# https://github.com/orgs/supabase/discussions/27071 Using SQLAlchemy with Supabase
def get_connection(connection: Union[Database, LocalDatabase]):
    """
    Obtiene un motor de base de datos (engine) de SQLAlchemy según el tipo de conexión proporcionada.
    """
    engine = create_engine(connection.__str__(), connect_args={'options': '-c timezone=utc'}) if isinstance(connection, Database) else create_engine(connection.__str__())
    Base.metadata.create_all(engine)
    
    return engine