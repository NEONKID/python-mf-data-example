from pymfdata.rdb.connection import Base
from sqlalchemy import BigInteger, String, Column, Text
from sqlalchemy.orm import relationship
from typing import Union, List

from common.seedwork.infrastructure.mixin import TimestampMixin


class MemoEntity(Base, TimestampMixin):
    __tablename__ = 'memo'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True, comment="Memo ID")
    title: Union[str, Column] = Column(String(255), nullable=False, comment="Memo Title")
    content: Union[str, Column] = Column(Text, nullable=True, comment="Memo body := content")
    r_labels = relationship('LabelEntity', secondary="memo_labels", lazy='noload')

    @property
    def labels(self):
        return self.r_labels

    @labels.setter
    def labels(self, labels_in: List[str]):
        from common.modules.label.infrastructure.entity import LabelEntity
        if labels_in:
            self.r_labels = list(map(lambda label: LabelEntity(name=label), labels_in))
