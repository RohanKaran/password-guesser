from fastapi import Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import api
from app.api.service import Service
from app.models import get_db
from app.schemas.level import LevelBase, Level


@api.post("/guess", response_model=Level)
async def guess_password(
    db: AsyncSession = Depends(get_db), level_in: LevelBase = Body(...)
):
    return await Service.guess_password(db, level_in)


@api.post("/response")
async def get_response(
    db: AsyncSession = Depends(get_db),
    query: str = Body(..., min_length=1, max_length=1000),
    level: int = Body(..., ge=1, le=3),
):
    return await Service.get_response(db, query, level)
