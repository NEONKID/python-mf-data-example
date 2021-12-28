from pydantic import Field
from typing import List, Optional

from common.modules.label.domain.value_object import MemoModel
from common.seedwork.domain.response import BaseORMResponse


class LabelResponse(BaseORMResponse):
    name: str = Field(title="Label name")
    memos: Optional[List[MemoModel]] = Field(title="Memo List")


class LabelSingleResponse(BaseORMResponse):
    name: str = Field(title="Label name")
    memo_count: int = Field(title="Memo count")
