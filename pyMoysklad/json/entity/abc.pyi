from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.client import JSONApi


class Object(DataClassJSONMixin): ...
class ObjectMixin(JSONApi): ...