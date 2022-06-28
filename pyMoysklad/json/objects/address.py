from dataclasses import dataclass

from pyMoysklad.json.utils.types import MetaInMeta
from pyMoysklad.json.entity import object


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
