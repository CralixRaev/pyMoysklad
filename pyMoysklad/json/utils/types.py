from collections import namedtuple
from datetime import datetime
from typing import TypeVar, Generic

from mashumaro.types import SerializableType

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta

T = TypeVar('T', bound=abc.Entity)


class CollectionAnswer(Generic[T]):
    def __init__(self, context: dict, meta: Meta, rows: list[T]) -> None:
        self.context = context
        self.meta = meta
        self._rows = rows

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        raise NotImplementedError

    def __str__(self) -> str:
        return f'CollectionAnswer: {self.rows}'

    def __repr__(self) -> str:
        return self.__str__()


class DateTime(datetime, SerializableType):
    def _serialize(self) -> dict[str, int]:
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "second": self.second,
        }

    @classmethod
    def _deserialize(cls, value: str):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

