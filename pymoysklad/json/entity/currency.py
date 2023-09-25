from dataclasses import dataclass
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.types import CollectionAnswer


@dataclass
class Unit(object.Object):
    gender: GenderEnum | None = None
    s1: str | None = None
    s2: str | None = None
    s5: str | None = None


@dataclass
class MajorUnit(Unit):
    pass


@dataclass
class MinorUnit(Unit):
    pass


@dataclass(repr=False)
class Currency(object.Entity):
    archived: bool | None = None
    code: str | None = None
    default: bool | None = None
    fullName: str | None = None
    indirect: bool | None = None
    isoCode: str | None = None
    majorUnit: MajorUnit | None = None
    minorUnit: MinorUnit | None = None
    margin: float | None = None
    multiplicity: int | None = None
    name: str | None = None
    rate: float | None = None
    rateUpdateType: str | None = None
    system: bool | None = None


class CurrencyMethods(object.ObjectMethods):
    NAME = "currency"

    def list_currency(self, **kwargs) -> CollectionAnswer[Currency]:
        return self.client.get_collection(self.NAME, Currency, **kwargs)

    def get_currency(self, uuid: UUID) -> Currency:
        return self.client.get_entity(self.NAME, Currency, uuid)

    def create_currency(self, currencies: Currency | list[Currency]):
        if isinstance(currencies, list):
            return self.client.mass_create_entity(self.NAME, currencies)
        else:
            return self.client.create_entity(self.NAME, currencies)

    def delete_currency(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_currency(self, uuid, currency: Currency) -> Currency:
        return self.client.edit_entity(self.NAME, currency, uuid)

    def mass_delete_currency(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
