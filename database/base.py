"""
Модуль конфигурации базы данных.

Содержит настройки подключения к PostgreSQL и базовые компоненты для работы
с SQLAlchemy в асинхронном режиме. Настроен пул соединений для оптимальной
производительности приложения.
"""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL


# Конфигурация URL подключения к базе данных PostgreSQL
url = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="postgres",
)

# Асинхронный движок SQLAlchemy с настроенным пулом соединений
engine = create_async_engine(url, pool_size=25, max_overflow=50, pool_timeout=300)

# Фабрика асинхронных сессий для работы с базой данных
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit=False)

# Базовый класс для всех моделей SQLAlchemy
Base = declarative_base()
