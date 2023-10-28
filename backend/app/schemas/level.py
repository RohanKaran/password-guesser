from pydantic import BaseModel, Field


class LevelBase(BaseModel):
    level: int = Field(..., ge=1, le=3)
    password: str = Field(..., min_length=5, max_length=10)


class LevelCreate(LevelBase):
    pass


class LevelUpdate(LevelBase):
    pass


class Level(LevelBase):
    class Config:
        from_attributes = True
