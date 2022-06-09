from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer


NAME = "country"


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
        return self._get_collection(NAME, Country, **kwargs)

    def get_country(self, uuid: UUID) -> Country:
        return self._get_entity(NAME, Country, uuid)

    def create_country(self, countries: Country | list[Country]):
        if isinstance(countries, list):
            return self._mass_create_entity(NAME, countries)
        else:
            return self._create_entity(NAME, countries)

    def delete_country(self, uuid: UUID):
        return self._delete_entity(NAME, uuid)

    def edit_country(self, uuid, country: Country) -> Country:
        return self._edit_entity(NAME, country, uuid)

    def mass_delete_country(self, metas: list[Meta]):
        return self._mass_delete_entity(NAME, metas)
