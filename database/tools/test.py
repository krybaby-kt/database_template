"""
Модуль инструментов для работы с тестовой моделью.

Содержит класс TestTool для выполнения CRUD операций 
с тестовыми записями в базе данных.
"""
from database.basic_tools import AsyncBaseIdSQLAlchemyCRUD
from database.models.test import TestModel
from asyncio import Lock


class TestTool(AsyncBaseIdSQLAlchemyCRUD):
    """
    Инструмент для работы с тестовой моделью TestModel.
    
    Предоставляет CRUD операции для тестовых записей с поддержкой
    асинхронных операций и блокировок для обеспечения целостности данных.
    
    Attributes:
        model: Модель данных TestModel
        field_id: Имя поля идентификатора ("id")
        lock: Асинхронная блокировка для синхронизации доступа
    """
    model = TestModel
    field_id = "id"
    lock: Lock = Lock()


    @staticmethod
    async def get_by_status(status: str) -> list[TestModel]:
        """
        Получает записи по статусу.
        
        Args:
            status: Статус записи
            
        Returns:
            List[TestModel]: Список записей
        """
        return await TestTool.get_all_with_filters(filters=[TestModel.status == status])
    
    async def update_count(self, count: int):
        """
        Обновляет счетчик записи.
        
        Args:
            count: Счетчик записи
            
        Returns:
            None
        """
        await self.update(data={"count": count})