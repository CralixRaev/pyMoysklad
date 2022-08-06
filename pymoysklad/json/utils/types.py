from dataclasses import dataclass
from typing import TypeVar, Generic

from mashumaro.types import SerializableType

from pymoysklad.json.entity import object
from pymoysklad.json.entity.object import Object
from pymoysklad.json.meta import Meta

T = TypeVar('T', bound=object.Entity)


@dataclass(repr=False)
class CollectionAnswer(Generic[T], Object):
    meta: Meta
    rows: list[T]
    context: dict | None = None

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
