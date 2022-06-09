from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer


@dataclass(repr=False)
class Country(abc.Object):
    externalCode: str = None
    id: UUID = None
    name: str = None
    updated: DateTime = None
    code: str = None
    description: str = None
    group: Meta = None
    owner: Meta = None
    shared: bool = None
    accountId: UUID = None


class CountryMixin(abc.ObjectMixin):
    def list_country(self) -> CollectionAnswer:
        return self._get_collection("entity/country", Country)
