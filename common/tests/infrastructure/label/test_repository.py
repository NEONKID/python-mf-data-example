import pytest
from faker import Faker

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.label.infrastructure.repository import LabelRepositoryProtocol

from common.tests import test_db_connect as db, AsyncSQLAlchemy, ko_faker, en_faker
from common.tests.infrastructure.label import get_label_repository as label_repo


@pytest.mark.asyncio
async def test_fetch_all(en_faker: Faker, ko_faker: Faker, label_repo: LabelRepositoryProtocol, db: AsyncSQLAlchemy):
    # given
    entity_list = list(map(lambda md: LabelEntity(name=md), en_faker.words()))

    async with db.session() as session:
        session.add_all(entity_list)
        await session.commit()

    # when
    label_list = await label_repo.fetch_all()

    # then
    for label in label_list:
        assert not label.memos


@pytest.mark.asyncio
async def test_fetch_by_name(en_faker: Faker, label_repo: LabelRepositoryProtocol, db: AsyncSQLAlchemy):
    # given
    label_name = en_faker.word()
    entity = LabelEntity(name=label_name)

    async with db.session() as session:
        session.add(entity)
        await session.commit()
        await session.refresh(entity)

    # when
    label = await label_repo.fetch_by_name(label_name)

    # then
    assert label.name == entity.name
