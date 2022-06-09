from dataclasses import dataclass
from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.meta import Meta
from pyMoysklad.json.utils.mixins import SkipDefaultFieldsReprMixin


@dataclass(repr=False)
class Object(SkipDefaultFieldsReprMixin, DataClassJSONMixin):
    meta: Meta = None


class ObjectMixin:
    pass
