from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.utils.types import DateTime


class TariffEnum(Enum):
    BASIC = "BASIC"
    CORPORATE = "CORPORATE"
    FREE = "FREE"
    MINIMAL = "MINIMAL"
    PROFESSIONAL = "PROFESSIONAL"
    RETAIL = "RETAIL"
    START = "START"
    TRIAL = "TRIAL"


@dataclass(repr=False)
class Subscription(abc.Object):
    # мойсклад... господи... ПОЧЕМУ???
    subscriptionEndDate: datetime = field(default=None, metadata={
        "deserialize": lambda l: datetime.utcfromtimestamp(l // 1000).replace(
            microsecond=l % 1000 * 1000)
    })
    role: str = None
    tariff: TariffEnum = None
    isSubscriptionChangeAvailable: bool = None


class SubscriptionMixin(abc.ObjectMixin):
    def get_subscription(self) -> Subscription:
        answer_raw = self.requester.get("accountSettings/subscription")
        return Subscription.from_dict(answer_raw)

