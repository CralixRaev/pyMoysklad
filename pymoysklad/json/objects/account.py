from dataclasses import dataclass

from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.types import MetaInMeta
from pymoysklad.json.entity import object


@dataclass(repr=False, frozen=True)
class Account(object.Object):
    accountNumber: str | None = None
    agent: Meta | None = None
    bankLocation: str | None = None
    bankName: str | None = None
    bic: str | None = None
    correspondentAccount: str | None = None
    isDefault: bool | None = None
