from typing import Any

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declared_attr, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    id: Any
    __name__: str
    # Generate tablename automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
