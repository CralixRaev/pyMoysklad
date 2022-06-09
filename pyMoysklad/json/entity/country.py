from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import DateTime


@dataclass(repr=False)
class Country(abc.Object):
    externalCode: str
    id: UUID
    name: str
    updated: DateTime
    code: str | None = None
    description: str | None = None
    group: Meta | None = None
    owner: Meta | None = None
    shared: bool | None = None
    accountId: UUID | None = None


class CountryMixin(abc.ObjectMixin):
    def list_country(self):
        answer = self.requester.get("entity/country")
        return [Country.from_dict(row) for row in answer['rows']]
