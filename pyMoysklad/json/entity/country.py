from dataclasses import dataclass
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.types import DateTime


@dataclass(repr=False)
class Country(abc.Object):
    externalCode: str
    id: UUID
    name: str
    updated: DateTime
    code: str | None = None
    description: str | None = None
    group: Meta | None = None
    owner: Meta | None = None
    shared: bool | None = None
