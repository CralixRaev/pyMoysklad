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
    subscriptionEndDate: datetime | None = field(default=None, metadata={
        "deserialize": lambda l: datetime.utcfromtimestamp(l // 1000).replace(
            microsecond=l % 1000 * 1000)
    })
    role: str | None = None
    tariff: TariffEnum | None = None
    isSubscriptionChangeAvailable: bool | None = None


class SubscriptionMethods(abc.ObjectMethods):
    def get_subscription(self) -> Subscription:
        answer_raw = self.client.requester.get("accountSettings/subscription")
        return Subscription.from_dict(answer_raw)

