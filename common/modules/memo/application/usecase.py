from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork
from pymfdata.rdb.transaction import async_transactional

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.label.infrastructure.repository import LabelRepositoryProtocol, LabelRepository
from common.modules.memo.domain.dto import MemoRegister, MemoUpdate
from common.modules.memo.domain.exception import MemoNotFoundException
from common.modules.memo.infrastructure.entity import MemoEntity
from common.modules.memo.infrastructure.repository import MemoRepositoryProtocol, MemoRepository


class MemoUseCaseUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self):
        await super().__aenter__()

        self.label_repository: LabelRepositoryProtocol = LabelRepository(self.session)
        self.memo_repository: MemoRepositoryProtocol = MemoRepository(self.session)


class MemoUseCase(BaseUseCase):
    def __init__(self, uow: MemoUseCaseUnitOfWork) -> None:
        self._uow: MemoUseCaseUnitOfWork = uow

    # @property
    # def uow(self) -> MemoUseCaseUnitOfWork:
    #     assert self._uow is not None
    #     return self._uow

    @async_transactional()
    async def create_memo(self, req: MemoRegister) -> MemoEntity:
        entity = MemoEntity(**req.dict())
        if entity.r_labels:
            for i in range(len(entity.r_labels)):
                item = await self.uow.label_repository.find_by_pk(entity.r_labels[i].name.strip())
                if item:
                    entity.r_labels[i] = item

        self.uow.memo_repository.create(entity)
        return entity

    @async_transactional()
    async def update_memo(self, item_id: int, req: MemoUpdate):
        entity = await self.uow.memo_repository.find_by_pk(item_id)
        if entity is None:
            raise MemoNotFoundException(item_id)

        label_list = []
        if req.labels:
            for i in range(len(req.labels)):
                label_item = await self.uow.label_repository.find_by_pk(req.labels[i].strip())
                if label_item:
                    label_list.append(label_item)
                else:
                    label_list.append(LabelEntity(name=req.labels[i].strip()))

            req.labels = None

        self.uow.memo_repository.update(entity, req.dict())
        if label_list:
            entity.r_labels = label_list

    @async_transactional()
    async def delete_memo(self, item_id: int):
        item = await self.uow.memo_repository.find_by_pk(item_id)
        if item is None:
            raise MemoNotFoundException(item_id)

        await self.uow.memo_repository.delete(item)

    @async_transactional(read_only=True)
    async def fetch_by_id(self, item_id: int):
        return await self.uow.memo_repository.fetch_by_id(item_id)

    @async_transactional(read_only=True)
    async def fetch_all(self):
        return await self.uow.memo_repository.fetch_all()
