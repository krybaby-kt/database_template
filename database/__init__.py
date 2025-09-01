"""
Модуль инициализации базы данных.

Этот модуль содержит функцию для инициализации моделей базы данных
и создания необходимых таблиц в PostgreSQL.
"""
from database.base import engine, Base

# Импортируем модели для автоматического создания таблиц в базе данных
from database.models.test import TestModel


async def init_models():
    """
    Инициализирует модели базы данных.
    
    Создает все таблицы в базе данных на основе определенных моделей SQLAlchemy.
    Использует асинхронное подключение для выполнения операций создания таблиц.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
