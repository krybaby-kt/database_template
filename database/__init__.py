from database.base import engine, Base

# Импортируем модели для автоматического создания таблиц в базе данных
from database.models.test import TestModel


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
