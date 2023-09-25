from dataclasses import dataclass, field
from datetime import datetime

from pymoysklad.json.entity import object
from pymoysklad.json.enums import TariffEnum


@dataclass(repr=False)
class Subscription(object.Object):
    # мойсклад... господи... ПОЧЕМУ???
    subscriptionEndDate: datetime | None = field(
        default=None,
        metadata={
            "deserialize": lambda x: datetime.utcfromtimestamp(x // 1000).replace(
                microsecond=x % 1000 * 1000
            )
        },
    )
    role: str | None = None
    tariff: TariffEnum | None = None
    isSubscriptionChangeAvailable: bool | None = None


class SubscriptionMethods(object.ObjectMethods):
    def get_subscription(self) -> Subscription:
        answer_raw = self.client.requester.get("accountSettings/subscription")
        return Subscription.from_dict(answer_raw)
