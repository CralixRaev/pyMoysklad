from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.utils.types import DateTime


@dataclass(repr=False)
class Region(abc.Object):
    externalCode: str
    id: UUID
    name: str
    updated: DateTime
    version: int | None = None
    accountId: UUID | None = None
    code: str | None = None


class RegionMixin(abc.ObjectMixin):
    def list_region(self):
        answer = self.requester.get("entity/region")
        return [Region.from_dict(row) for row in answer['rows']]