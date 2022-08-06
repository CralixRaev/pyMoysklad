from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.entity.counterparty import Counterparty
from pymoysklad.json.entity.product import Product
from pymoysklad.json.entity.variant import Variant
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta, MetaArray
from pymoysklad.json.utils.api_types.DateTime import DateTime
from pymoysklad.json.utils.types import CollectionAnswer, MetaInMeta


# TODO: Refactor (create some common functions for working with documents and expand)
def product_or_variant(raw: dict) -> Product | Variant:
    if raw['meta']['type'] == 'product':
        return Product.from_dict(raw)
    else:
        return Variant.from_dict(raw)


@dataclass(repr=False)
class SupplyPosition(object.Entity):
    quantity: float | int | None = None
    price: float | int | None = None
    discount: float | int | None = None
    vat: float | int | None = None
    vatEnabled: bool | None = None
    assortment: Meta | Product | Variant | None = field(
        metadata={
            "serialize": lambda v: {'meta': v.to_dict()},
            "deserialize": product_or_variant
        },
        default=None
    )
    # gtd: ...
    country: MetaInMeta | None = None
    overhead: float | int | None = None


@dataclass(repr=False)
class Supply(object.Entity):
    agent: Counterparty | MetaInMeta | None = None
    agentAccount: MetaInMeta | None = None
    applicable: bool | None = None
    # attributes: ...
    code: str | None = None
    contract: MetaInMeta | None = None
    created: DateTime | None = None
    deleted: DateTime | None = None
    description: str | None = None
    files: MetaArray | None = None
    group: MetaInMeta | None = None
    id: UUID | None = None
    incomingDate: DateTime | None = None
    incomingNumber: str | None = None
    moment: DateTime | None = None
    name: str | None = None
    organization: MetaInMeta | None = None
    organizationAccount: MetaInMeta | None = None
    # overhead: ...
    owner: MetaInMeta | None = None
    payedSum: float | None = None
    positions: MetaArray | None = None
    printed: bool | None = None
    project: MetaInMeta | None = None
    published: bool | None = None
    # rate: ...
    shared: bool | None = None
    state: MetaInMeta | None = None
    store: MetaInMeta | None = None
    sum: int | None = None
    syncId: UUID | None = None
    vatEnabled: bool | None = None
    vatIncluded: bool | None = None
    vatSum: float | None = None


class SupplyMethods(object.ObjectMethods):
    NAME = "supply"

    def list_supply(self, **kwargs) -> CollectionAnswer[Supply]:
        return self.client.get_collection(self.NAME, Supply, **kwargs)

    def get_supply(self, uuid: UUID) -> Supply:
        return self.client.get_entity(self.NAME, Supply, uuid)

    def create_supply(self, supplies: Supply | list[Supply]):
        if isinstance(supplies, list):
            return self.client.mass_create_entity(self.NAME, supplies)
        else:
            return self.client.create_entity(self.NAME, supplies)

    def delete_supply(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_supply(self, uuid, supply: Supply) -> Supply:
        return self.client.edit_entity(self.NAME, supply, uuid)

    def mass_delete_supply(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)

    def list_supply_positions(self, uuid: UUID, **kwargs) -> CollectionAnswer[SupplyPosition]:
        return self.client.get_collection(f'{self.NAME}/{uuid}/positions', SupplyPosition, **kwargs)

    def create_supply_positions(self, supply_uuid: UUID,
                                positions: SupplyPosition | list[SupplyPosition]):
        if isinstance(positions, list):
            return self.client.mass_create_entity(f'{self.NAME}/{supply_uuid}/positions', positions)
        else:
            return self.client.create_entity(f'{self.NAME}/{supply_uuid}/positions', positions)
