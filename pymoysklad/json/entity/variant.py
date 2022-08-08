from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.entity.product import Product
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta, MetaArray
from pymoysklad.json.objects.images import Image
from pymoysklad.json.objects.sale_price import SalePrice
from pymoysklad.json.utils.types import CollectionAnswer, MetaInMeta


@dataclass(repr=False)
class Variant(object.Entity):
    archived: bool | None = None
    article: str | None = None
    # barcodes: ...
    # buyPrice: ...
    # characteristics: ...
    code: str | None = None
    discountProhibited: bool | None = None
    images: CollectionAnswer[Image] | MetaArray | None = None
    # minPrice: ...
    name: str | None = None
    # packs: ...
    product: Product | MetaInMeta | None = None
    salePrices: list[SalePrice] | None = None
    things: list[str] | None = None


class VariantMethods(object.ObjectMethods):
    NAME = "variant"

    def list_variant(self, **kwargs) -> CollectionAnswer[Variant]:
        return self.client.get_collection(self.NAME, Variant, **kwargs)

    def get_variant(self, uuid: UUID) -> Variant:
        return self.client.get_entity(self.NAME, Variant, uuid)

    def create_variant(self, currencies: Variant | list[Variant]):
        if isinstance(currencies, list):
            return self.client.mass_create_entity(self.NAME, currencies)
        else:
            return self.client.create_entity(self.NAME, currencies)

    def delete_variant(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_variant(self, uuid, currency: Variant) -> Variant:
        return self.client.edit_entity(self.NAME, currency, uuid)

    def mass_delete_variant(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
