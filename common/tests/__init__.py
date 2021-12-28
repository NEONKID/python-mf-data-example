import os
import sys
import pytest

from asyncio import get_event_loop
from dotenv import dotenv_values
from faker import Factory
from faker.generator import Generator
from pymfdata.rdb.connection import AsyncSQLAlchemy, Base

sys.path.append(os.path.dirname(os.getcwd()))

env_prefix = sys.path[0] + '/common/resources/.env.'
env = dotenv_values(env_prefix + 'test')
db = AsyncSQLAlchemy(db_uri='postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
    env['DB_USER'], env['DB_PASSWORD'], env['DB_HOST'], env['DB_PORT'], env['DB_NAME']))


@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def ko_faker() -> Generator:
    return Factory.create('ko_KR')


@pytest.fixture(scope="session")
def en_faker() -> Generator:
    return Factory.create('en_US')


@pytest.fixture(scope="session")
async def test_db_connect():
    if db._session_factory is None:
        await db.connect(
            connect_args={
                "server_settings": {
                    "application_name": "Python Micro Framework Data FastAPI Example Test Runner"
                }}
        )
        db.init_session_factory()

        async with db._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    yield db

    if db._session_factory is not None:
        await db.disconnect()
