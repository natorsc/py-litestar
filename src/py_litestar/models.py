from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, text
from sqlmodel import Field, SQLModel


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(SQLModel):
    created_at: datetime = Field(
        default_factory=utcnow,
        sa_type=DateTime(timezone=True),
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=utcnow,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"onupdate": text("(CURRENT_TIMESTAMP)")},
        nullable=False,
    )
    active: bool = Field(default=True, nullable=False)


class Task(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=255)
    done: bool = Field(default=False, nullable=False)
