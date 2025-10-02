"""
Модуль тестовой модели для демонстрации работы с базой данных.

Содержит модель TestModel для тестирования функционала CRUD операций
и демонстрации работы с SQLAlchemy в асинхронном режиме.
"""
from database.base_model import SQLAlchemyModel
from sqlalchemy import BigInteger, Column, String, DateTime, Integer
import datetime


class TestModel(SQLAlchemyModel):
    """
    Тестовая модель для демонстрации работы с базой данных.
    
    Attributes:
        id (BigInteger): Уникальный идентификатор записи (первичный ключ)
        status (String): Статус тестовой записи
        count (Integer): Числовое значение для тестирования
        creating_date (DateTime): Дата и время создания записи
    """
    __tablename__ = "tests"
    id = Column(BigInteger, unique=True, primary_key=True)

    status = Column(String, default=None)
    count = Column(Integer, default=None)

    creating_date = Column(DateTime, default=datetime.datetime.now)
