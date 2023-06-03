from dataclasses import dataclass, field
from uuid import UUID
from mashumaro import field_options

from pymoysklad.json.entity import object
from pymoysklad.json.entity.productfolder import ProductFolder
from pymoysklad.json.meta import Meta, MetaArray
from pymoysklad.json.objects.barcode import Barcode
from pymoysklad.json.objects.images import Image
from pymoysklad.json.objects.sale_price import SalePrice
from pymoysklad.json.utils.types import CollectionAnswer, MetaInMeta


@dataclass(repr=False)
class Product(object.Entity):
    # alcoholic: ...
    archived: bool | None = None
    article: str | None = None
    # attributes: ...
    barcodes: list[Barcode] | None = None
    # buyPrice: ...
    code: str | None = None
    country: Meta | None = None
    description: str | None = None
    discountProhibited: bool | None = None
    effectiveVat: int | None = None
    effectiveVatEnabled: bool | None = None
    files: MetaArray | None = None
    group: Meta | None = None
    id_: UUID | None = field(metadata=field_options(alias="id"), default=None)
    images: CollectionAnswer[Image] | MetaArray | None = None
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
    productFolder: ProductFolder | MetaInMeta | None = None
    salePrices: list[SalePrice] | None = None
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

    def create_product(self, products: Product | list[Product]):
        if isinstance(products, list):
            return self.client.mass_create_entity(self.NAME, products)
        else:
            return self.client.create_entity(self.NAME, products)

    def delete_product(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_product(self, uuid, currency: Product) -> Product:
        return self.client.edit_entity(self.NAME, currency, uuid)

    def mass_delete_product(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
