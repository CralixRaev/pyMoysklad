from dataclasses import dataclass, field


from mashumaro.config import BaseConfig, TO_DICT_ADD_OMIT_NONE_FLAG
from mashumaro.mixins.json import DataClassJSONMixin
from mashumaro.types import SerializableType, GenericSerializableType

from pymoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin


@dataclass(repr=False)
class Meta(DataClassJSONMixin, SkipDefaultFieldsReprMixin):
    href: str | None = None
    metadataHref: str | None = None
    downloadHref: str | None = None
    type: str | None = None
    mediaType: str | None = "application/json"
    uuidHref: str | None = None

    def _serialize(self) -> dict:
        return self.to_dict()

    class Config(BaseConfig):
        code_generation_options = [TO_DICT_ADD_OMIT_NONE_FLAG]


@dataclass(repr=False)
class MetaArray(Meta):
    size: int | None = None
    limit: int | None = None
    offset: int | None = None
    nextHref: str | None = None
    previousHref: str | None = None