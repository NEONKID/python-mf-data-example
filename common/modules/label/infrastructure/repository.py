from pymfdata.rdb.repository import AsyncRepository, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import contains_eager
from typing import List

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.memo.infrastructure.entity import MemoEntity


class LabelRepositoryProtocol(AsyncRepository[LabelEntity, str]):
    async def fetch_all(self) -> List[LabelEntity]:
        ...

    async def fetch_by_name(self, item_name: str) -> LabelEntity:
        ...


class LabelRepository(LabelRepositoryProtocol):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_all(self) -> List[LabelEntity]:
        stmt = self._gen_stmt_for_param().order_by(self._model.memo_count.desc())

        result = await self.session.execute(stmt)
        return result.unique().scalars().fetchall()

    async def fetch_by_name(self, item_name: str) -> LabelEntity:
        stmt = select(self._model).outerjoin(self._model.memos).where(self._model.name == item_name).options(
            contains_eager(self._model.memos)
        ).order_by(MemoEntity.updated_at.desc())

        result = await self.session.execute(stmt)
        return result.unique().scalars().one_or_none()
