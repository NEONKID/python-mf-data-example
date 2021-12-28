from pydantic import Field

from common.config.base import BaseSettings


class DatabaseSettings(BaseSettings):
    engine: str = Field(default="postgresql+asyncpg", env="DB_ENGINE")
    host: str = Field(default="localhost", env="DB_HOST")
    port: int = Field(default=5432, env="DB_PORT")
    name: str = Field(default=None, env="DB_NAME")
    username: str = Field(default="postgres", env="DB_USER")
    password: str = Field(default="postgres", env="DB_PASSWORD")
