from uuid import UUID
from abc import ABC
from dataclasses import dataclass

from mashumaro.config import BaseConfig, TO_DICT_ADD_OMIT_NONE_FLAG
from mashumaro.mixins.json import DataClassJSONMixin

from pymoysklad.json.meta import Meta
from pymoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin
from pymoysklad.json.utils.api_types.DateTime import DateTime


@dataclass(repr=False)
class Object(ABC, SkipDefaultFieldsReprMixin, DataClassJSONMixin):
    class Config(BaseConfig):
        code_generation_options = [TO_DICT_ADD_OMIT_NONE_FLAG]


@dataclass(repr=False)
class Entity(Object):
    meta: Meta | None = None
    id: UUID | None = None
    updated: DateTime = None
    accountId: UUID | None = None
    externalCode: str | None = None


class ObjectMethods:
    def __init__(self, client):
        self.client = client
