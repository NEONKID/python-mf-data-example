from pymfdata.rdb.connection import Base
from sqlalchemy import BigInteger, Column, ForeignKey, func, select, String, Table, PrimaryKeyConstraint
from sqlalchemy.orm import column_property, relationship
from typing import Union

from common.modules.memo.infrastructure.entity import MemoEntity


memo_labels = Table('memo_labels', Base.metadata,
                    Column('memo_id', BigInteger, ForeignKey("memo.id")),
                    Column('label_name', String(64), ForeignKey("label.name", ondelete="RESTRICT")),
                    PrimaryKeyConstraint('memo_id', 'label_name'))


class LabelEntity(Base):
    __tablename__ = 'label'

    name: Union[str, Column] = Column(String(64), primary_key=True, nullable=False)
    memos = relationship('MemoEntity', viewonly=True, secondary='memo_labels', uselist=True, lazy='noload')

    memo_count = column_property(select([func.count()]).select_from(memo_labels).where(
        memo_labels.c.label_name == name).correlate_except(MemoEntity.__table__).scalar_subquery())
