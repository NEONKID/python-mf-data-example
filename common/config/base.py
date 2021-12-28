import os
from pydantic import BaseSettings as _BaseSettings


class BaseSettings(_BaseSettings):
    class Config:
        env_file = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)))) + '/common/resources/.env.{}'.format(os.environ.get('APP_ENV', 'dev'))
        env_file_encoding = 'utf-8'
