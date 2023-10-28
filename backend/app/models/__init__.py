import random
import string
from typing import Generator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.models.base import Base
from app.models.level import Level

engine = create_async_engine(
    "sqlite+aiosqlite:///./test.db",
    pool_pre_ping=True,
    connect_args={"check_same_thread": False},  # for sqlitedB
)
SessionLocal = async_sessionmaker(bind=engine)


def generate_random_string():
    length = random.randint(5, 10)
    result = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    return result


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as db:
        try:
            if await db.get(Level, 1) is None:
                db.add(Level(level=1, password=generate_random_string()))

            if await db.get(Level, 2) is None:
                db.add(Level(level=2, password=generate_random_string()))

            if await db.get(Level, 3) is None:
                db.add(Level(level=3, password=generate_random_string()))
        except SQLAlchemyError as e:
            print(e)
        finally:
            await db.commit()
            await db.close()


async def get_db() -> Generator[AsyncSession, None, None]:
    """
    Get a database connection
    """
    try:
        db: AsyncSession = SessionLocal()
        yield db
    finally:
        await db.close()
