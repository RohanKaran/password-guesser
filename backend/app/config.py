from pydantic_settings import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    DATABASE_URI: str = "sqlite+aiosqlite:///./test.db"
    OPENAI_API_KEY: str = "OPENAI_API_KEY"


config = Config()
