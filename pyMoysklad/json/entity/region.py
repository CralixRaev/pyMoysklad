from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer


@dataclass(repr=False)
class Region(abc.Object):
    externalCode: str | None = None
    id: UUID | None = None
    name: str | None = None
    updated: DateTime | None = None
    version: int | None = None
    accountId: UUID | None = None
    code: str | None = None


class RegionMethods(abc.ObjectMethods):
    NAME = "region"

    def list_region(self, **kwargs) -> CollectionAnswer[Region]:
        return self.client.get_collection(self.NAME, Region, **kwargs)

    def get_region(self, uuid: UUID) -> Region:
        return self.client.get_entity(self.NAME, Region, uuid)
