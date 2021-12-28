import os
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton
from pymfdata.rdb.connection import AsyncSQLAlchemy

from common.config import ApplicationSettings


class BaseContainer(DeclarativeContainer):
    config = Configuration()
    config.from_pydantic(ApplicationSettings(_env_file=os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))) + '/resources/.env.{}'.format(os.environ.get('APP_ENV', 'dev'))))

    db = Singleton(AsyncSQLAlchemy, db_uri='{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        engine=config.db.engine(), username=config.db.username(), password=config.db.password(),
        host=config.db.host(), port=config.db.port(), db_name=config.db.name()))
