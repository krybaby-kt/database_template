from database.basic_tools import AsyncBaseIdSQLAlchemyCRUD
from database.models.test import TestModel
from asyncio import Lock


class TestTool(AsyncBaseIdSQLAlchemyCRUD):
    model = TestModel
    field_id = "id"
    lock: Lock = Lock()
