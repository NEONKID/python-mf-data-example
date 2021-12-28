from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declared_attr


class TimestampMixin:
    @declared_attr
    def created_at(self) -> Column:
        return Column(DateTime(timezone=True), nullable=False, default=func.now())

    @declared_attr
    def updated_at(self) -> Column:
        return Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
