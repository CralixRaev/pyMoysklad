from dataclasses import dataclass

from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import MetaInMeta
from pyMoysklad.json.entity import object


@dataclass(repr=False)
class Account(object.Object):
    accountNumber: str | None = None
    agent: Meta | None = None
    bankLocation: str | None = None
    bankName: str | None = None
    bic: str | None = None
    correspondentAccount: str | None = None
    isDefault: bool | None = None
