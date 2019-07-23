from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from setting import Base
from setting import ENGINE

class User(Base):
    """
    UserModel
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)