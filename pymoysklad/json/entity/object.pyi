from abc import ABC

from mashumaro.mixins.json import DataClassJSONMixin

from pymoysklad.json.client import JSONApi

class Object(ABC, DataClassJSONMixin): ...
class Entity(Object): ...

class ObjectMethods:
    def __init__(self, client: JSONApi):
        self.client = client
