from mashumaro.mixins.json import DataClassJSONMixin

from pyMoysklad.json.client import JSONApi


class Object(DataClassJSONMixin): ...
class Entity(Object): ...
class ObjectMethods:
    def __init__(self, client: JSONApi):
        self.client = client