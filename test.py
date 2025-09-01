import asyncio
import database
from database.tools.test import TestTool
from database.models.test import TestModel


async def test():
    await database.init_models()
    dbTest: TestModel = await TestTool.create(data={"status": "test", "count": 1})
    test = await TestTool(dbTest.id).get()
    print(await TestTool.get_all())

if __name__ == "__main__":
    asyncio.run(test())