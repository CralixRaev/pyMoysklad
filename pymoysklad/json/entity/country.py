from dataclasses import dataclass
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.types import CollectionAnswer


@dataclass(repr=False)
class Country(object.Entity):
    name: str | None = None
    code: str | None = None
    description: str | None = None
    group: Meta | None = None
    owner: Meta | None = None
    shared: bool | None = None


class CountryMethods(object.ObjectMethods):
    NAME = "country"

    def list_country(self, **kwargs) -> CollectionAnswer[Country]:
        return self.client.get_collection(self.NAME, Country, **kwargs)

    def get_country(self, uuid: UUID) -> Country:
        return self.client.get_entity(self.NAME, Country, uuid)

    def create_country(
        self, countries: Country | list[Country]
    ) -> list[Country] | Country:
        if isinstance(countries, list):
            return self.client.mass_create_entity(self.NAME, countries)
        else:
            return self.client.create_entity(self.NAME, countries)

    def delete_country(self, uuid: UUID) -> None:
        return self.client.delete_entity(self.NAME, uuid)

    def edit_country(self, uuid, country: Country) -> Country:
        return self.client.edit_entity(self.NAME, country, uuid)

    def mass_delete_country(self, metas: list[Meta]) -> list[dict]:
        return self.client.mass_delete_entity(self.NAME, metas)
