import pytest
from httpx import AsyncClient

from common.tests import en_faker, ko_faker

from fastapi_app.src.asgi import api


@pytest.fixture(scope="session")
async def test_client() -> AsyncClient:
    async with AsyncClient(app=api, base_url='http://test') as client:
        yield client
