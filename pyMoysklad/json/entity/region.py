from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer


@dataclass(repr=False)
class Region(abc.Object):
    externalCode: str = None
    id: UUID = None
    name: str = None
    updated: DateTime = None
    version: int = None
    accountId: UUID = None
    code: str = None


class RegionMixin(abc.ObjectMixin):
    def list_region(self) -> CollectionAnswer:
        return self._get_collection("entity/country", Region)

