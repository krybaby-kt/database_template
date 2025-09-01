from database.basic_model import SQLAlchemyModel
from sqlalchemy import BigInteger, Column, String, DateTime, Integer
import datetime


class TestModel(SQLAlchemyModel):
    __tablename__ = "tests"
    id = Column(BigInteger, unique=True, primary_key=True)

    status = Column(String, default=None)
    count = Column(Integer, default=None)

    creating_date = Column(DateTime, default=datetime.datetime.now)
