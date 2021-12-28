from enum import Enum

from common.config.base import BaseSettings
from common.config.cors import CORSSettings
from common.config.database import DatabaseSettings
from common.config.log import LogSettings


class ApplicationEnvironment(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class ApplicationSettings(BaseSettings):
    cors: CORSSettings = CORSSettings()
    db: DatabaseSettings = DatabaseSettings()
    log: LogSettings = LogSettings()
