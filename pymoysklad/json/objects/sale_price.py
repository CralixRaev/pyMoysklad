from dataclasses import dataclass
from pymoysklad.json.entity import object
from pymoysklad.json.entity.currency import Currency
from pymoysklad.json.entity.pricetype import PriceType
from pymoysklad.json.meta import Meta


@dataclass(repr=False)
class SalePrice(object.Object):
    value: float | None = None
    currency: Currency | Meta | None = None
    priceType: PriceType | None = None
