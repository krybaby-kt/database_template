# Database Template

A comprehensive Python template for asynchronous database operations using SQLAlchemy and PostgreSQL. This template provides a robust foundation for building database-driven applications with async/await support, automatic retry mechanisms, and dynamic filtering capabilities.

## Features

- 🚀 **Async/Await Support** - Full asynchronous database operations
- 🔄 **Automatic Retry Logic** - Built-in error handling with configurable retry attempts
- 🔍 **Dynamic Filtering** - Flexible query building with multiple filter conditions
- 📊 **Sorting & Pagination** - Built-in support for data sorting and pagination
- 🏗️ **Repository Pattern** - Clean separation of database logic
- 🔒 **Connection Pooling** - Optimized database connection management
- 📝 **Type Hints** - Full typing support for better code quality

## Project Structure

```
database_template/
├── database/
│   ├── __init__.py          # Database initialization
│   ├── base.py              # Database configuration and connection
│   ├── basic_model.py       # Base model class
│   ├── basic_tools.py       # Repository classes and CRUD operations
│   ├── models/
│   │   └── test.py          # Example model
│   └── tools/
│       └── test.py          # Example repository
├── test.py                  # Usage example
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/database_template.git
cd database_template
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure database connection in `database/base.py`:
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

## Quick Start

### 1. Define Your Model

```python
from database.basic_model import SQLAlchemyModel
from sqlalchemy import Column, BigInteger, String, Integer

class YourModel(SQLAlchemyModel):
    __tablename__ = "your_table"
    
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    value = Column(Integer)
```

### 2. Create Repository

```python
from database.basic_tools import AsyncBaseIdSQLAlchemyCRUD
from your_model import YourModel

class YourTool(AsyncBaseIdSQLAlchemyCRUD):
    model = YourModel
    field_id = "id"
```

### 3. Use in Application

```python
import asyncio
import database
from your_tool import YourTool

async def main():
    # Initialize database tables
    await database.init_models()
    
    # Create record
    record = await YourTool.create(data={"name": "example", "value": 42})
    
    # Get record by ID
    found_record = await YourTool(record.id).get()
    
    # Get all records with filters
    filtered_records = await YourTool.get_all_with_filters(
        filters=[YourModel.value > 10],
        sort_by="name",
        limit=10
    )
    
    # Update record
    await YourTool(record.id).update({"value": 100})
    
    # Delete record
    await YourTool(record.id).delete()

if __name__ == "__main__":
    asyncio.run(main())
```

## Core Components

### AsyncAbstractRepository
Abstract base class defining the repository interface with all necessary CRUD operations.

### AsyncSQLAlchemyRepository
Base implementation of the repository pattern with SQLAlchemy support, providing:
- Basic CRUD operations
- Dynamic filtering and sorting
- Batch operations

### AsyncBaseIdSQLAlchemyCRUD
Enhanced repository with ID-based operations, featuring:
- Automatic retry mechanism (configurable attempts)
- Unique ID generation
- Session management
- Error handling and logging

### SQLAlchemyModel
Base model class with convenient string representation methods for debugging and logging.

## Advanced Features

### Dynamic Filtering
```python
# Multiple filter conditions
records = await YourTool.get_all_with_filters(
    filters=[
        YourModel.status == "active",
        YourModel.created_date > datetime.now() - timedelta(days=7),
        YourModel.value.between(10, 100)
    ]
)
```

### Sorting and Pagination
```python
# Sorted and paginated results
records = await YourTool.get_all_with_filters(
    sort_by="created_date",
    sort_order="desc",
    limit=20,
    offset=40
)
```

### Batch Operations
```python
# Update multiple records
await YourTool.update_with_filters(
    data={"status": "processed"},
    filters=[YourModel.status == "pending"]
)

# Delete multiple records
await YourTool.delete_with_filters(
    filters=[YourModel.created_date < old_date]
)
```

### Custom Repository Methods
Extend repositories with custom methods:

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

## Configuration

### Database Connection
Configure your database connection in `database/base.py`:

```python
# Connection pool settings
engine = create_async_engine(
    url, 
    pool_size=25,           # Number of connections to maintain
    max_overflow=50,        # Additional connections when pool is full
    pool_timeout=300        # Timeout for getting connection from pool
)
```

### Retry Settings
Configure retry attempts for operations:

```python
class YourTool(AsyncBaseIdSQLAlchemyCRUD):
    model = YourModel
    field_id = "id"
    count_attemps = 5  # Number of retry attempts
```

## Requirements

- Python 3.8+
- PostgreSQL 12+
- See `requirements.txt` for Python dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
