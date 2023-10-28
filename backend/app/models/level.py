from sqlalchemy import Integer, Column, String

from app.models.base import Base


class Level(Base):
    level = Column(Integer, nullable=False, primary_key=True)
    password = Column(String(10), nullable=False)

    def __init__(self, **kwargs) -> None:
        super(Level, self).__init__(**kwargs)
