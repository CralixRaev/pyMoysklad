from dataclasses import dataclass

from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin


@dataclass(repr=False)
class Meta(DataClassJSONMixin, SkipDefaultFieldsReprMixin):
    href: str
    metadataHref: str | None = None
    downloadHref: str | None = None
    type: str | None = None
    mediaType: str | None = "application/json"
    uuidHref: str | None = None


@dataclass
class MetaArray(Meta):
    size: int | None = None
    limit: int | None = None
    offset: int | None = None
    nextHref: str | None = None
    previousHref: str | None = None
