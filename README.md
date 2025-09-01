# Database Template

Комплексный Python шаблон для асинхронных операций с базой данных с использованием SQLAlchemy и PostgreSQL. Данный шаблон предоставляет надежную основу для создания приложений, работающих с базами данных, с поддержкой async/await, автоматическими механизмами повторных попыток и возможностями динамической фильтрации.

## Возможности

- 🚀 **Поддержка Async/Await** - Полностью асинхронные операции с базой данных
- 🔄 **Автоматическая логика повторов** - Встроенная обработка ошибок с настраиваемым количеством попыток
- 🔍 **Динамическая фильтрация** - Гибкое построение запросов с множественными условиями фильтрации
- 📊 **Сортировка и пагинация** - Встроенная поддержка сортировки данных и пагинации
- 🏗️ **Паттерн Repository** - Четкое разделение логики работы с базой данных
- 🔒 **Пулинг соединений** - Оптимизированное управление соединениями с базой данных
- 📝 **Типизация** - Полная поддержка типов для лучшего качества кода

## Структура проекта

```
database_template/
├── database/
│   ├── __init__.py          # Инициализация базы данных
│   ├── base.py              # Конфигурация базы данных и соединение
│   ├── basic_model.py       # Базовый класс модели
│   ├── basic_tools.py       # Классы репозиториев и CRUD операции
│   ├── models/
│   │   └── test.py          # Пример модели
│   └── tools/
│       └── test.py          # Пример репозитория
├── test.py                  # Пример использования
├── requirements.txt         # Зависимости
└── README.md               # Этот файл
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/database_template.git
cd database_template
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте соединение с базой данных в `database/base.py`:
```python
url = URL.create(
    drivername="postgresql+asyncpg",
    username="your_username",
    password="your_password",
    host="localhost",
    port="5432",
    database="your_database",
)
```

## Быстрый старт

### 1. Определите вашу модель

```python
from database.basic_model import SQLAlchemyModel
from sqlalchemy import Column, BigInteger, String, Integer

class YourModel(SQLAlchemyModel):
    __tablename__ = "your_table"
    
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    value = Column(Integer)
```

### 2. Создайте репозиторий

```python
from database.basic_tools import AsyncBaseIdSQLAlchemyCRUD
from your_model import YourModel

class YourTool(AsyncBaseIdSQLAlchemyCRUD):
    model = YourModel
    field_id = "id"
```

### 3. Используйте в приложении

```python
import asyncio
import database
from your_tool import YourTool

async def main():
    # Инициализация таблиц базы данных
    await database.init_models()
    
    # Создание записи
    record = await YourTool.create(data={"name": "example", "value": 42})
    
    # Получение записи по ID
    found_record = await YourTool(record.id).get()
    
    # Получение всех записей с фильтрами
    filtered_records = await YourTool.get_all_with_filters(
        filters=[YourModel.value > 10],
        sort_by="name",
        limit=10
    )
    
    # Обновление записи
    await YourTool(record.id).update({"value": 100})
    
    # Удаление записи
    await YourTool(record.id).delete()

if __name__ == "__main__":
    asyncio.run(main())
```

## Основные компоненты

### AsyncAbstractRepository
Абстрактный базовый класс, определяющий интерфейс репозитория со всеми необходимыми CRUD операциями.

### AsyncSQLAlchemyRepository
Базовая реализация паттерна репозиторий с поддержкой SQLAlchemy, предоставляющая:
- Основные CRUD операции
- Динамическая фильтрация и сортировка
- Пакетные операции

### AsyncBaseIdSQLAlchemyCRUD
Расширенный репозиторий с операциями на основе ID, включающий:
- Автоматический механизм повторов (настраиваемое количество попыток)
- Генерация уникальных ID
- Управление сессиями
- Обработка ошибок и логирование

### SQLAlchemyModel
Базовый класс модели с удобными методами строкового представления для отладки и логирования.

## Расширенные возможности

### Динамическая фильтрация
```python
# Множественные условия фильтрации
records = await YourTool.get_all_with_filters(
    filters=[
        YourModel.status == "active",
        YourModel.created_date > datetime.now() - timedelta(days=7),
        YourModel.value.between(10, 100)
    ]
)
```

### Сортировка и пагинация
```python
# Отсортированные и пагинированные результаты
records = await YourTool.get_all_with_filters(
    sort_by="created_date",
    sort_order="desc",
    limit=20,
    offset=40
)
```

### Пакетные операции
```python
# Обновление нескольких записей
await YourTool.update_with_filters(
    data={"status": "processed"},
    filters=[YourModel.status == "pending"]
)

# Удаление нескольких записей
await YourTool.delete_with_filters(
    filters=[YourModel.created_date < old_date]
)
```

### Пользовательские методы репозитория
Расширяйте репозитории пользовательскими методами:

```python
class YourTool(AsyncBaseIdSQLAlchemyCRUD):
    model = YourModel
    field_id = "id"
    
    @staticmethod
    async def get_by_status(status: str) -> list[YourModel]:
        return await YourTool.get_all_with_filters(
            filters=[YourModel.status == status]
        )
    
    async def increment_value(self, amount: int = 1):
        current = await self.get()
        await self.update({"value": current.value + amount})
```

## Конфигурация

### Соединение с базой данных
Настройте соединение с базой данных в `database/base.py`:

```python
# Настройки пула соединений
engine = create_async_engine(
    url, 
    pool_size=25,           # Количество соединений для поддержания
    max_overflow=50,        # Дополнительные соединения при переполнении пула
    pool_timeout=300        # Таймаут для получения соединения из пула
)
```

### Настройки повторов
Настройка количества попыток для операций:

```python
class YourTool(AsyncBaseIdSQLAlchemyCRUD):
    model = YourModel
    field_id = "id"
    count_attemps = 5  # Количество попыток повтора
```

## Требования

- Python 3.8+
- PostgreSQL 12+
- См. `requirements.txt` для зависимостей Python

## Участие в разработке

1. Сделайте форк репозитория
2. Создайте ветку для новой функциональности
3. Внесите изменения
4. Добавьте тесты, если применимо
5. Отправьте pull request

## Поддержка

Если у вас возникли проблемы или есть вопросы, пожалуйста, создайте issue на GitHub.
