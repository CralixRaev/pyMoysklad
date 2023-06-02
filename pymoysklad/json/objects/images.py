from dataclasses import dataclass

from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.api_types.DateTime import DateTime
from pymoysklad.json.utils.types import MetaInMeta
from pymoysklad.json.entity import object


@dataclass(repr=False)
class Image(object.Object):
    filename: str | None = None
    meta: Meta | None = None
    miniature: Meta | None = None
    size: int | None = None
    tiny: Meta | None = None
    title: str | None = None
    updated: DateTime | None = None
