import uuid
from sqlmodel import SQLModel, Field
from enum import auto, StrEnum


class StatusEnum(StrEnum):
    CREATED = auto()
    RUNNING = auto()
    FAILED = auto()


class NotFoundError(Exception):
    pass


class DBTask(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    status: StatusEnum = Field(default=StatusEnum.CREATED, nullable=False)


class CSVData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_id: uuid.UUID | None = Field(default=None, foreign_key="dbtask.id")
    country: str = Field(default="None", nullable=False)
    latitude: str = Field(default="None", nullable=False)
    longitude: str = Field(default="None", nullable=False)
