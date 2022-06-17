from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from pyMoysklad.json.entity import object
from pyMoysklad.json.meta import Meta, MetaArray
from pyMoysklad.json.utils.types import DateTime, CollectionAnswer, MetaInMeta


class CompanyType(Enum):
    LEGAL = "legal"
    ENTREPRENEUR = "entrepreneur"
    INDIVIDUAL = "individual"


@dataclass(repr=False)
class Address(object.Object):
    addInfo: str | None = None
    apartment: str | None = None
    city: str | None = None
    comment: str | None = None
    country: MetaInMeta | None = None
    house: str | None = None
    postalCode: str | None = None
    region: MetaInMeta | None = None
    street: str | None = None


@dataclass(repr=False)
class SignStamp(object.Entity):
    title: str | None = None
    filename: str | None = None
    size: int | None = None
    updated: DateTime | None = None
    miniature: Meta | None = None


@dataclass(repr=False)
class Organization(object.Entity):
    accountId: UUID | None = None
    actualAddress: str | None = None
    actualAddressFull: Address | None = None
    archived: bool | None = None
    bonusPoints: int | None = None
    bonusProgram: MetaInMeta | None = None
    code: str | None = None
    companyType: str | None = None
    created: DateTime | None = None
    description: str | None = None
    externalCode: str | None = None
    group: MetaInMeta | None = None
    id: UUID | None = None
    name: str | None = None
    owner: MetaInMeta | None = None
    shared: bool | None = None
    syncId: UUID | None = None
    trackingContractDate: DateTime | None = None
    trackingContractNumber: int | None = None
    updated: DateTime | None = None
    certificateDate: DateTime | None = None
    certificateNumber: str | None = None
    chiefAccountant: str | None = None
    accounts: MetaArray | None = None
    attributes: list[Meta] | None = None
    chiefAccountSign: SignStamp | None = None
    directorSign: SignStamp | None = None
    director: str | None = None
    directorPosition: str | None = None
    email: str | None = None
    fax: str | None = None
    fsrarId: str | None = None
    inn: str | None = None
    isEgaisEnable: bool | None = None
    kpp: str | None = None
    legalAddress: str | None = None
    legalAddressFull: Address | None = None
    legalFirstName: str | None = None
    legalLastName: str | None = None
    legalMiddleName: str | None = None
    legalTitle: str | None = None
    ogrn: str | None = None
    ogrnip: str | None = None
    okpo: str | None = None
    payerVat: bool | None = None
    phone: str | None = None
    stamp: str | None = None
    utmUrl: str | None = None


class OrganizationMethods(object.ObjectMethods):
    NAME = "organization"

    def list_organization(self, **kwargs) -> CollectionAnswer[Organization]:
        return self.client.get_collection(self.NAME, Organization, **kwargs)

    def get_organization(self, uuid: UUID) -> Organization:
        return self.client.get_entity(self.NAME, Organization, uuid)

    def create_organization(self, organizations: Organization | list[Organization]):
        if isinstance(organizations, list):
            return self.client.mass_create_entity(self.NAME, organizations)
        else:
            return self.client.create_entity(self.NAME, organizations)

    def delete_organization(self, uuid: UUID):
        return self.client.delete_entity(self.NAME, uuid)

    def edit_organization(self, uuid, organization: Organization) -> Organization:
        return self.client.edit_entity(self.NAME, organization, uuid)

    def mass_delete_organization(self, metas: list[Meta]):
        return self.client.mass_delete_entity(self.NAME, metas)
