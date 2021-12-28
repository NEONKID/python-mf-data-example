from pydantic import Field

from common.config.base import BaseSettings


class LogSettings(BaseSettings):
    level: str = Field(default="debug", env="LOG_LEVEL")
