"""
Модуль демонстрации функционала базы данных.

Содержит примеры использования инструментов для работы с базой данных,
включая создание записей, получение данных и вывод результатов.
"""
import asyncio
import database
from database.tools.test import TestTool
from database.models.test import TestModel


async def test():
    """
    Демонстрирует основные операции с базой данных.
    
    Выполняет следующие действия:
    1. Инициализирует модели базы данных
    2. Создает тестовую запись
    3. Получает созданную запись по ID
    4. Выводит все записи из таблицы
    """
    await database.init_models()
    dbTest: TestModel = await TestTool.create(data={"status": "test", "count": 1})
    test = await TestTool(dbTest.id).get()
    print(await TestTool.get_all())

if __name__ == "__main__":
    asyncio.run(test())