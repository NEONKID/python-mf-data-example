import pytest
from faker import Faker

from common.modules.memo.infrastructure.entity import MemoEntity
from common.modules.memo.infrastructure.repository import MemoRepositoryProtocol

from common.tests import test_db_connect as db, AsyncSQLAlchemy, ko_faker, en_faker
from common.tests.infrastructure.memo import get_memo_repository as memo_repo


@pytest.mark.asyncio
async def test_fetch_all(en_faker: Faker, ko_faker: Faker, db: AsyncSQLAlchemy, memo_repo: MemoRepositoryProtocol):
    # given
    data = [
        {
            'title': en_faker.sentence(),
            'content': en_faker.text(),
            'labels': en_faker.words()
        }
        for _ in range(3)
    ]
    entities = list(map(lambda md: MemoEntity(**md), data))

    async with db.session() as session:
        session.add_all(entities)
        await session.commit()

    # when
    result = await memo_repo.fetch_all()

    # then
    for memo in result:
        assert not memo.labels


@pytest.mark.asyncio
async def test_fetch_by_id(en_faker: Faker, ko_faker: Faker, db: AsyncSQLAlchemy, memo_repo: MemoRepositoryProtocol):
    # given
    item_id = en_faker.random_int(1, 3)

    # when
    result = await memo_repo.fetch_by_id(item_id)

    # then
    assert result.id == item_id
