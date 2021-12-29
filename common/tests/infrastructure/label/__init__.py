import pytest
from common.tests import AsyncSQLAlchemy

from common.modules.label.infrastructure.repository import LabelRepository


@pytest.fixture(scope="session")
async def get_label_repository(db: AsyncSQLAlchemy):
    async with db.session() as session:
        yield LabelRepository(session)
