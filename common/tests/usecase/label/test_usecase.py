import pytest
from faker import Faker
from unittest.mock import AsyncMock

from common.modules.label.application.usecase import LabelUseCase, LabelUseCaseUnitOfWork
from common.modules.label.domain.dto import LabelResponse, LabelSingleResponse
from common.modules.label.infrastructure.repository import LabelEntity
from common.modules.label.infrastructure.repository import LabelRepositoryProtocol

from common.tests import en_faker, ko_faker

_repository_mock = AsyncMock(spec=LabelRepositoryProtocol)

_uow_mock = AsyncMock(spec=LabelUseCaseUnitOfWork)
_uow_mock.label_repository = _repository_mock


@pytest.mark.asyncio
async def test_fetch_all(en_faker: Faker, ko_faker: Faker):
    # given
    data = [
        {
            'name': en_faker.word(),
            'memo_count': en_faker.random_int(0, 65535),
        }
        for _ in range(255)
    ]
    entity_list = list(map(lambda md: LabelEntity(**md), data))

    _repository_mock.fetch_all.return_value = entity_list
    _usecase = LabelUseCase(_uow_mock)

    # when
    result = await _usecase.fetch_all()

    # then
    list(map(lambda model: LabelSingleResponse.from_orm(model), result))
    _repository_mock.fetch_all.assert_called_once_with()


@pytest.mark.asyncio
async def test_fetch_by_name(en_faker: Faker, ko_faker: Faker):
    # given
    data = {
        'name': en_faker.word(),
        'memos': [
            {
                'id': en_faker.random_int(1, 65535),
                "title": en_faker.sentence(),
                "content": en_faker.text()
            }
            for _ in range(15)
        ]
    }
    entity = LabelEntity(**data)

    _repository_mock.fetch_by_name.return_value = entity
    _usecase = LabelUseCase(_uow_mock)

    # when
    result = await _usecase.fetch_by_name(data['name'])

    # then
    LabelResponse.from_orm(entity)
    _repository_mock.fetch_by_name.assert_called_once_with(data['name'])
