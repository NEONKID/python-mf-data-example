from pydantic import Field
from typing import Optional

from common.seedwork.domain.response import BaseORMResponse


class LabelInfo(BaseORMResponse):
    name: str = Field(title="Label name")
    memo_count: Optional[int] = Field(title="Memo count")
