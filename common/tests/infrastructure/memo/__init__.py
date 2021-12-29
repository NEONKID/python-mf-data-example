import pytest
from common.tests import AsyncSQLAlchemy

from common.modules.memo.infrastructure.repository import MemoRepository


@pytest.fixture(scope="session")
async def get_memo_repository(db: AsyncSQLAlchemy):
    async with db.session() as session:
        yield MemoRepository(session)
