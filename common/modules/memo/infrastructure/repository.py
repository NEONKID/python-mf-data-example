from pymfdata.rdb.repository import AsyncRepository, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import contains_eager
from typing import List, Optional

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.memo.infrastructure.entity import MemoEntity


class MemoRepositoryProtocol(AsyncRepository[MemoEntity, int]):
    async def fetch_all(self) -> List[MemoEntity]:
        ...

    async def fetch_by_id(self, item_id: int) -> Optional[MemoEntity]:
        ...


class MemoRepository(MemoRepositoryProtocol):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_all(self) -> List[MemoEntity]:
        stmt = select(self._model)

        result = await self.session.execute(stmt)
        return result.unique().scalars().fetchall()

    async def fetch_by_id(self, item_id: int) -> Optional[MemoEntity]:
        stmt = self._gen_stmt_for_param(id=item_id).options(
            contains_eager(self._model.r_labels).load_only(LabelEntity.name, LabelEntity.memo_count)
        ).order_by(LabelEntity.memo_count.desc())

        result = await self.session.execute(stmt)
        return result.unique().scalars().one_or_none()
