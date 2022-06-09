from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer


@dataclass(repr=False)
class Country(abc.Object):
    externalCode: str | None = None
    id: UUID | None = None
    name: str | None = None
    updated: DateTime | None = None
    code: str | None = None
    description: str | None = None
    group: Meta | None = None
    owner: Meta | None = None
    shared: bool | None = None
    accountId: UUID | None = None


class CountryMixin(abc.ObjectMixin):
    def list_country(self, **kwargs) -> CollectionAnswer:
        return self._get_collection("entity/country", Country, **kwargs)

    def get_country(self, uuid: UUID) -> Country:
        return self._get_entity("entity/country", Country, uuid)

    def create_country(self, countries: Country | list[Country]):
        if isinstance(countries, list):
            return self._mass_create_entity("entity/country", countries)
        else:
            return self._create_entity("entity/country", countries)
