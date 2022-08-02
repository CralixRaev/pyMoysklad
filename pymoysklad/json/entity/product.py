from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta, MetaArray
from pymoysklad.json.utils.types import CollectionAnswer


@dataclass(repr=False)
class Product(object.Entity):
    # alcoholic: ...
    archived: bool | None = None
    article: str | None = None
    # attributes: ...
    # barcodes: ...
    # buyPrice: ...
    code: str | None = None
    country: Meta | None = None
    description: str | None = None
    discountProhibited: bool | None = None
    effectiveVat: int | None = None
    effectiveVatEnabled: bool | None = None
    files: MetaArray | None = None
    group: Meta | None = None
    images: MetaArray | None = None
    isSerialTrackable: bool | None = None
    # minPrice: ...
    minimumBalance: int | None = None
    name: str | None = None
    owner: Meta | None = None
    # packs: ...
    partialDisposal: bool | None = None
    pathName: str | None = None
    paymentItemType: str | None = None  # TODO: create enum
    ppeType: str | None = None  # TODO: create enum
    productFolder: Meta | None = None
    # salePrices: ...
    shared: bool | None = None
    supplier: Meta | None = None
    syncId: UUID | None = None
    taxSystem: str | None = None  # TODO: create enum
    things: list[str] | None = None
    tnved: str | None = None
    trackingType: str | None = None  # TODO: create enum
    uom: Meta | None = None
    useParentVat: bool | None = None
    variantsCount: int | None = None
    vat: int | None = None
    vatEnabled: bool | None = None
    volume: int | None = None
    weight: int | None = None


class ProductMethods(object.ObjectMethods):
    NAME = "product"

    def list_product(self, **kwargs) -> CollectionAnswer[Product]:
        return self.client.get_collection(self.NAME, Product, **kwargs)

    def get_product(self, uuid: UUID) -> Product:
        return self.client.get_entity(self.NAME, Product, uuid)

    def create_product(self, currencies: Product | list[Product]):
        if isinstance(currencies, list):
            return self.client.mass_create_entity(self.NAME, currencies)
        else:
            return self.client.create_entity(self.NAME, currencies)

    def delete_product(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_product(self, uuid, currency: Product) -> Product:
        return self.client.edit_entity(self.NAME, currency, uuid)

    def mass_delete_product(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
