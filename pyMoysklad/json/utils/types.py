from collections import namedtuple
from datetime import datetime
from mashumaro.types import SerializableType


CollectionAnswer = namedtuple("CollectionAnswer", ["context", "meta", "rows"])


class DateTime(datetime, SerializableType):
    def _serialize(self) -> dict[str, int]:
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "second": self.second,
        }

    @classmethod
    def _deserialize(cls, value: str):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

