import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from unittest import TestCase

from common.tests import en_faker, ko_faker
from common.tests import test_db_connect

from fastapi_app.src.app import create_app


@pytest.fixture(scope="session")
async def test_client() -> AsyncClient:
    api = create_app()
    async with AsyncClient(app=api, base_url='http://localhost:5001') as client, LifespanManager(api):
        yield client
