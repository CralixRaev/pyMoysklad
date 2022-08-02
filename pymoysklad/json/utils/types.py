from abc import ABC
from collections import namedtuple
from datetime import datetime
from typing import TypeVar, Generic, Any

from mashumaro.types import SerializableType, SerializationStrategy

from pymoysklad.json.entity import object
from pymoysklad.json.meta import Meta


T = TypeVar('T', bound=object.Entity)


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


# i hate moysklad
class MetaInMeta(Meta, SerializableType):
    def _serialize(self) -> dict:
        return {
            'meta': super().to_dict()
        }

    @classmethod
    def _deserialize(cls, value: dict[str, dict]) -> Meta:
        return Meta.from_dict(value['meta'])
