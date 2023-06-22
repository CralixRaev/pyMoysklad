from datetime import datetime

from mashumaro.types import SerializableType


class DateTime(datetime, SerializableType):
    def _serialize(self) -> str:
        return self.strftime("%Y-%m-%d %H:%M:%S.%f")

    @classmethod
    def _deserialize(cls, value: str):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
