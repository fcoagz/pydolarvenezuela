from typing import Any, List, Union, Optional
from datetime import datetime
from sqlalchemy import Column, Integer, func
from sqlalchemy.orm import Session

from .models import Page, Monitor, Currency, MonitorPriceHistory
from .engine import get_connection, create_tables
from ..models import Page as SchemaPage
from ..models import Monitor as SchemaMonitor

class DatabaseSettings:
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
    
    def add_price_history(self, monitor_id: int, price: float, last_update: datetime) -> None:
        """
        Agrega el historial de precios de un monitor.
        """
        with Session(self.engine) as session:
            new_price_history = MonitorPriceHistory(monitor_id=monitor_id, price=price, last_update=last_update)
            session.add(new_price_history)
            session.commit()

    def get_date_range_history(self, page_id: int, currency_id: int, type_monitor: str, start_date: datetime, end_date: datetime):
        """
        Obtiene el historial de precios de un monitor en un rango de fechas.
        """
        with Session(self.engine) as session:
            monitor = session.query(Monitor).filter(
                Monitor.page_id == page_id,
                Monitor.currency_id == currency_id,
                Monitor.key == type_monitor).first()

            if not monitor:
                return None

            changes = {}
            query = session.query(MonitorPriceHistory).\
                filter(
                    MonitorPriceHistory.monitor_id == monitor.id,
                    func.date(MonitorPriceHistory.last_update) >= start_date, 
                    func.date(MonitorPriceHistory.last_update) <= end_date).order_by(MonitorPriceHistory.last_update.desc()).all()

            for price_history in query:
                changes[price_history.last_update] = price_history
            
            return changes.values()
    
    def get_prices_monitor_one_day(self, page_id: int, currency_id: int, type_monitor: str, last_update: datetime):
        """
        Obtiene el historial de precios de un monitor en una fecha especifica.
        """
        with Session(self.engine) as session:
            monitor = session.query(Monitor).filter(
                Monitor.page_id == page_id,
                Monitor.currency_id == currency_id,
                Monitor.key == type_monitor).first()
            
            if not monitor:
                return None

            return session.query(MonitorPriceHistory).\
                filter(
                    MonitorPriceHistory.monitor_id == monitor.id,
                    func.date(MonitorPriceHistory.last_update) == last_update).all()

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

    def update_monitor(self, id: int,
                    price: float,
                    price_old: Optional[float],
                    percent: float,
                    change: float,
                    color: str,
                    symbol: str,
                    last_update: str, 
                    image: str) -> None:
        """
        Actualiza un monitor en la base de datos según el ID proporcionado.
        """
        with Session(self.engine) as session:
            session.query(Monitor).filter(Monitor.id == id).update({
                'price': price,
                'price_old': price_old,
                'percent': percent,
                'change': change,
                'color': color,
                'symbol': symbol,
                'last_update': last_update,
                'image': image
            })
            session.commit()

    def get_monitors(self, page_id: int, currency_id: int) -> List[Monitor]:
        """
        Obtiene todos los monitores de una página según el ID de la página y la moneda.
        """
        with Session(self.engine) as session:
            return session.query(Monitor).filter(Monitor.page_id == page_id, Monitor.currency_id == currency_id).all()