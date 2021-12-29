import pytest
from faker import Faker
from unittest.mock import AsyncMock, MagicMock

from common.modules.memo.application.usecase import MemoUseCase, MemoUseCaseUnitOfWork
from common.modules.memo.domain.dto import MemoResponse, MemoSingleResponse, MemoRegister, MemoUpdate
from common.modules.memo.infrastructure.repository import MemoRepositoryProtocol, MemoEntity
from common.modules.label.infrastructure.repository import LabelRepositoryProtocol

from common.tests import en_faker, ko_faker
from common.tests.usecase import async_magic

_memo_repository_mock = AsyncMock(spec=MemoRepositoryProtocol)
_label_repository_mock = AsyncMock(spec=LabelRepositoryProtocol)

_uow_mock = AsyncMock(spec=MemoUseCaseUnitOfWork)
_uow_mock.memo_repository = _memo_repository_mock
_uow_mock.label_repository = _label_repository_mock

MagicMock.__await__ = lambda x: async_magic().__await__()


@pytest.mark.asyncio
async def test_create_memo(en_faker: Faker, ko_faker: Faker):
    # given
    data = {
        "id": en_faker.random_int(1, 65535),
        "title": en_faker.sentence(),
        "content": en_faker.text(),
        "labels": en_faker.words()
    }

    _memo_repository_mock.create.return_value = None
    _label_repository_mock.find_by_pk.return_value = None
    _usecase = MemoUseCase(_uow_mock)

    # when
    result = await _usecase.create_memo(MemoRegister(**data))

    # then
    assert result.title == data['title']


@pytest.mark.asyncio
async def test_update_memo(en_faker: Faker, ko_faker: Faker):
    # given
    item_id = en_faker.random_int(1, 65535)
    data = {
        'id': item_id,
        "title": en_faker.sentence(),
        "content": en_faker.text(),
        "labels": en_faker.words()
    }

    req = {
        "title": en_faker.sentence(),
        "content": en_faker.text(),
        "labels": en_faker.words()
    }
    entity = MemoEntity(**data)

    _memo_repository_mock.find_by_pk.return_value = entity
    _memo_repository_mock.update.return_value = None
    _usecase = MemoUseCase(_uow_mock)

    # when
    await _usecase.update_memo(item_id, MemoUpdate(**req))

    # then
    _memo_repository_mock.find_by_pk.assert_called_with(item_id)


@pytest.mark.asyncio
async def test_delete_memo(en_faker: Faker, ko_faker: Faker):
    # given
    data = {
        'id': en_faker.random_int(1, 65535),
        "title": en_faker.sentence(),
        "content": en_faker.text(),
        "labels": en_faker.words()
    }
    entity = MemoEntity(**data)

    _memo_repository_mock.find_by_pk.return_value = entity
    _memo_repository_mock.delete.return_value = None
    _usecase = MemoUseCase(_uow_mock)

    # when
    await _usecase.delete_memo(data['id'])

    # then
    _memo_repository_mock.find_by_pk.assert_called_with(data['id'])
    _memo_repository_mock.delete.assert_called_once_with(entity)


@pytest.mark.asyncio
async def test_fetch_all(en_faker: Faker, ko_faker: Faker):
    # given
    data_list = [
        {
            'id': en_faker.random_int(1, 65535),
            "title": en_faker.sentence(),
            "content": en_faker.text(),
            "labels": en_faker.words()
        }
        for _ in range(128)
    ]
    query_list = list(map(lambda md: MemoEntity(**md), data_list))

    _memo_repository_mock.fetch_all.return_value = query_list
    _usecase = MemoUseCase(_uow_mock)

    # when
    result = await _usecase.fetch_all()

    # then
    list(map(lambda response: MemoSingleResponse.from_orm(response), result))
    _memo_repository_mock.fetch_all.assert_called_once_with()


@pytest.mark.asyncio
async def test_fetch_by_id(en_faker: Faker, ko_faker: Faker):
    # given
    data = {
        'id': en_faker.random_int(1, 65535),
        "title": en_faker.sentence(),
        "content": en_faker.text(),
        "labels": en_faker.words()
    }
    entity = MemoEntity(**data)

    _memo_repository_mock.fetch_by_id.return_value = entity
    _usecase = MemoUseCase(_uow_mock)

    # when
    result = await _usecase.fetch_by_id(data['id'])

    # then
    MemoResponse.from_orm(result)
    _memo_repository_mock.fetch_by_id.assert_called_once_with(data['id'])
