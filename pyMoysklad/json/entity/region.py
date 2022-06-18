from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import object
from pyMoysklad.json.utils.types import CollectionAnswer


@dataclass(repr=False)
class Region(object.Entity):
    externalCode: str | None = None
    name: str | None = None
    version: int | None = None
    code: str | None = None


class RegionMethods(object.ObjectMethods):
    NAME = "region"

    def list_region(self, **kwargs) -> CollectionAnswer[Region]:
        return self.client.get_collection(self.NAME, Region, **kwargs)

    def get_region(self, uuid: UUID) -> Region:
        return self.client.get_entity(self.NAME, Region, uuid)
