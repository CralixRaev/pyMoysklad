from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.types import CollectionAnswer


@dataclass(repr=False)
class PriceType(object.Entity):
    name: str | None = None


class PriceTypeMethods(object.ObjectMethods):
    NAME = "companysettings/pricetype"

    def list_price_type(self, **kwargs) -> CollectionAnswer[PriceType]:
        return self.client.get_collection(self.NAME, PriceType, **kwargs, resource_name="context")

    def get_price_type(self, uuid: UUID) -> PriceType:
        return self.client.get_entity(self.NAME, PriceType, uuid, "context")

    def get_default_price_type(self) -> PriceType:
        return self.client.get_entity(self.NAME, PriceType, "default", "context")

    def create_price_type(self, price_types: PriceType | list[PriceType]):
        if isinstance(price_types, list):
            return self.client.mass_create_entity(self.NAME, price_types, "context")
        else:
            return self.client.create_entity(self.NAME, price_types, "context")
