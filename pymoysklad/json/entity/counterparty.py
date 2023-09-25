from dataclasses import dataclass
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.enums import CompanyType
from pymoysklad.json.meta import MetaArray, Meta
from pymoysklad.json.objects.address import Address
from pymoysklad.json.utils.api_types.DateTime import DateTime


@dataclass(repr=False)
class Counterparty(object.Entity):
    accounts: MetaArray | None = None
    actualAddress: str | None = None
    actualAddressFull: Address | None = None
    archived: bool | None = None
    bonusPoints: int | None = None
    bonusProgram: Meta | None = None
    code: str = None
    companyType: CompanyType | None = None
    description: str | None = None
    discountCardNumber: str | None = None
    email: str | None = None
    fax: str | None = None
    files: MetaArray | None = None
    group: Meta | None = None
    name: str | None = None
    owner: Meta | None = None
    phone: str | None = None
    salesAmount: int | None = None
    state: Meta | None = None
    syncId: UUID | None = None
    certificateDate: DateTime | None = None
    certificateNumber: str | None = None
    contactpersons: MetaArray | None = None
    # discounts: str | None = None
    inn: str | None = None
    kpp: str | None = None
    legalAddress: str | None = None
    legalAddressFull: Address | None = None
    legalFirstName: str | None = None
    legalLastName: str | None = None
    legalMiddleName: str | None = None
    legalTitle: str | None = None
    notes: MetaArray | None = None
    ogrn: str | None = None
    ogrnip: str | None = None
    okpo: str | None = None
    priceType: str = None  # TODO: PRICE OBJECT
    tags: list[str] | None = None


class CounterpartyMethods(object.ObjectMethods):
    NAME = "counterparty"
