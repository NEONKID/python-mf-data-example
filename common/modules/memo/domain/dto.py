from pydantic import BaseModel, Field
from typing import Optional, List

from common.modules.memo.domain.value_object import LabelInfo
from common.seedwork.domain.response import BaseORMResponse


class MemoRegister(BaseModel):
    title: str = Field(title="Memo title")
    content: Optional[str] = Field(title="Memo body")
    labels: Optional[List[str]] = Field(title="Memo labels")


class MemoUpdate(BaseModel):
    title: Optional[str] = Field(title="Memo title")
    content: Optional[str] = Field(title="Memo body")
    labels: Optional[List[str]] = Field(None, title="Memo labels")


class MemoResponse(BaseORMResponse):
    id: int = Field(title="Memo ID")
    title: str = Field(title="Memo title")
    content: Optional[str] = Field(title="Memo body")
    labels: Optional[List[LabelInfo]] = Field(title="Memo labels")


class MemoSingleResponse(BaseORMResponse):
    id: int = Field(title="Memo ID")
    title: str = Field(title="Memo title")
    content: Optional[str] = Field(title="Memo body")
