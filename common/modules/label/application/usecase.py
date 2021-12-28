from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork
from pymfdata.rdb.transaction import async_transactional

from common.modules.label.infrastructure.repository import LabelRepositoryProtocol, LabelRepository


class LabelUseCaseUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self):
        await super().__aenter__()

        self.label_repository: LabelRepositoryProtocol = LabelRepository(self.session)


class LabelUseCase(BaseUseCase):
    def __init__(self, uow: LabelUseCaseUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def fetch_all(self):
        return await self.uow.label_repository.fetch_all()

    @async_transactional(read_only=True)
    async def fetch_by_name(self, item_name: str):
        return await self.uow.label_repository.fetch_by_name(item_name)
