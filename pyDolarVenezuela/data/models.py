from sqlalchemy import String, Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Page(Base):
    __tablename__ = 'pages'

    id   = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url  = Column(String, nullable=False)

class Currency(Base):
    __tablename__ = 'currencies'

    id   = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)

class Monitor(Base):
    __tablename__ = 'monitors'

    id          = Column(Integer, primary_key=True)
    page_id     = Column(Integer, ForeignKey('pages.id'), nullable=False)
    currency_id = Column(Integer, ForeignKey('currencies.id'), nullable=False)
    key         = Column(String, nullable=True)
    title       = Column(String, nullable=False)
    price       = Column(Float, nullable=False)
    price_old   = Column(Float, nullable=True)
    last_update = Column(DateTime(timezone=True), nullable=False)
    image       = Column(String, nullable=True)
    percent     = Column(Float, nullable=True, default=0.0)
    change      = Column(Float, nullable=True, default=0.0)
    color       = Column(String, nullable=True, default="neutral")
    symbol      = Column(String, nullable=True, default="")

class MonitorPriceHistory(Base):
    __tablename__ = 'monitor_price_history'

    id          = Column(Integer, primary_key=True)
    monitor_id  = Column(Integer, ForeignKey('monitors.id'), nullable=False)
    price       = Column(Float, nullable=False)
    last_update = Column(DateTime(timezone=True), nullable=False)