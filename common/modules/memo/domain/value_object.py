from pydantic import Field

from common.seedwork.domain.response import BaseORMResponse


class LabelInfo(BaseORMResponse):
    name: str = Field(title="Label name")
    memo_count: int = Field(title="Memo count")
