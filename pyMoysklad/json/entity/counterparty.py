from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import object
from pyMoysklad.json.enums import CompanyType
from pyMoysklad.json.meta import MetaArray, Meta
from pyMoysklad.json.objects.address import Address
from pyMoysklad.json.utils.types import CollectionAnswer


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


class CounterpartyMethods(object.ObjectMethods):
    NAME = "counterparty"
