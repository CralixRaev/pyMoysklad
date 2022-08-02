from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import GenderEnum
from pymoysklad.json.meta import Meta, MetaArray
from pymoysklad.json.utils.api_types.DateTime import DateTime
from pymoysklad.json.utils.types import CollectionAnswer, MetaInMeta


@dataclass(repr=False)
class Supply(object.Entity):
    agent: MetaInMeta | None = None
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

    def create_supply(self, currencies: Supply | list[Supply]):
        if isinstance(currencies, list):
            return self.client.mass_create_entity(self.NAME, currencies)
        else:
            return self.client.create_entity(self.NAME, currencies)

    def delete_supply(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_supply(self, uuid, currency: Supply) -> Supply:
        return self.client.edit_entity(self.NAME, currency, uuid)

    def mass_delete_supply(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
