from typing import Any, List, Union
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session

from .models import Page, Monitor, Currency
from .engine import get_connection, create_tables
from ..models.pages import Page as SchemaPage
from ..models.monitor import Monitor as SchemaMonitor

class SettingsDB:
    def __init__(self, connection) -> None:
        """
        Configuracion de la base de datos.
        """
        self.engine = get_connection(connection)
        create_tables(self.engine)

    def get_or_create_page(self, page: SchemaPage) -> Union[Any, Column[Integer]]:
        """
        Obtiene el ID de la página, en caso contrario la crea y también devuelve el ID.
        """
        with Session(self.engine) as session:
            existing_page = session.query(Page).filter(Page.name == page.name).first()
            if existing_page:
                return existing_page.id
            else:
                new_page = Page(name=page.name, url=page.provider)
                session.add(new_page)
                session.commit()
                return new_page.id

    def get_or_create_currency(self, currency: str) -> Union[Any, Column[Integer]]:
        """
        Obtiene el ID de la moneda, en caso contrario la crea y también devuelve el ID.
        """
        with Session(self.engine) as session:
            existing_currency = session.query(Currency).filter(Currency.symbol == currency).first()
            if existing_currency:
                return existing_currency.id
            else:
                new_currency = Currency(symbol=currency)
                session.add(new_currency)
                session.commit()
                return new_currency.id


    def create_monitor(self, page_id: int, currency_id: int, monitor: SchemaMonitor) -> None:
        """
        Generar un monitor en la base de datos especificando el id de la página y la moneda.
        """
        with Session(self.engine) as session:
            existing_monitor = session.query(Monitor).filter(
                Monitor.page_id == page_id,
                Monitor.currency_id == currency_id,
                Monitor.title == monitor.title
            ).first()
            
            if not existing_monitor:
                new_monitor = Monitor(page_id=page_id, currency_id=currency_id, **monitor.__dict__)
                session.add(new_monitor)
                session.commit()

    def create_monitors(self, page_id: int, currency_id: int, monitors: List[SchemaMonitor]) -> None:
        """
        Generar varios monitores en la base de datos especificando el id de la página y la moneda.
        """
        with Session(self.engine) as session:
            existing_monitor = session.query(Monitor).filter(
                    Monitor.page_id == page_id,
                    Monitor.currency_id == currency_id
                ).first()

            if not existing_monitor:
                new_monitors = [Monitor(page_id=page_id, currency_id=currency_id, **monitor.__dict__)
                                for monitor in monitors]
                session.add_all(new_monitors)
                session.commit()

    def update_monitor(self, id: int, monitor: SchemaMonitor) -> None:
        """
        Actualiza un monitor en la base de datos según el ID proporcionado.
        """
        with Session(self.engine) as session:
            session.query(Monitor).filter(Monitor.id == id).update(monitor.__dict__)
            session.commit()
    
    def get_monitors(self, name: str) -> List[Monitor]:
        """
        Obtiene todos los monitores de una página según el nombre de la misma.
        """
        with Session(self.engine) as session:
            return session.query(Monitor).filter(Monitor.page_id == session.query(Page).filter(Page.name == name).first().id).all()