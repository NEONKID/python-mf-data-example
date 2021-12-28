from pydantic import Field
from typing import Optional

from common.seedwork.domain.response import BaseORMResponse


class MemoModel(BaseORMResponse):
    id: int = Field(title="Memo ID")
    title: str = Field(title="Memo title")
    content: Optional[str] = Field(title="Memo body")
