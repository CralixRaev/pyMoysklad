from dataclasses import dataclass

from pymoysklad.json.entity import object


@dataclass(repr=False, frozen=True)
class Barcode(object.Object):
    ean13: str | None = None
    ean8: str | None = None
    code128: str | None = None
    gtin: str | None = None
