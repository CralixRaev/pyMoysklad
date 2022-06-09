from dataclasses import dataclass

from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin


@dataclass(repr=False)
class Meta(DataClassJSONMixin, SkipDefaultFieldsReprMixin):
    href: str
    metadataHref: str = None
    downloadHref: str = None
    type: str = None
    mediaType: str = "application/json"
    uuidHref: str = None


@dataclass
class MetaArray(Meta):
    size: int = None
    limit: int = None
    offset: int = None
    nextHref: str = None
    previousHref: str = None
