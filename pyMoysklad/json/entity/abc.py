from dataclasses import dataclass

from mashumaro.config import BaseConfig, TO_DICT_ADD_OMIT_NONE_FLAG
from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin


@dataclass(repr=False)
class Object(SkipDefaultFieldsReprMixin, DataClassJSONMixin):

    class Config(BaseConfig):
        code_generation_options = [TO_DICT_ADD_OMIT_NONE_FLAG]


@dataclass(repr=False)
class Entity(Object):
    meta: Meta = None


class ObjectMethods:
    def __init__(self, client):
        self.client = client
