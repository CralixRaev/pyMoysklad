from typing import Type, TypeVar
from urllib.parse import urljoin
from uuid import UUID

from pymoysklad.json.entity import object
from pymoysklad.json.entity.country import Country, CountryMethods
from pymoysklad.json.entity.currency import CurrencyMethods
from pymoysklad.json.entity.organization import OrganizationMethods
from pymoysklad.json.entity.product import ProductMethods
from pymoysklad.json.entity.region import RegionMethods
from pymoysklad.json.entity.subscription import SubscriptionMethods
from pymoysklad.json.entity.supply import SupplyMethods
from pymoysklad.json.entity.variant import VariantMethods
from pymoysklad.json.meta import MetaArray, Meta
from pymoysklad.json.requester import Requester
from pymoysklad.json.utils.types import CollectionAnswer


T = TypeVar("T", bound=object.Entity)


class JSONApi:
    def __init__(self, auth: str | tuple[str, str]):
        self.requester: Requester = Requester(auth)

        self.country = CountryMethods(self)
        self.region = RegionMethods(self)
        self.currency = CurrencyMethods(self)
        self.subscription = SubscriptionMethods(self)
        self.organization = OrganizationMethods(self)
        self.product = ProductMethods(self)
        self.variant = VariantMethods(self)

        self.supply = SupplyMethods(self)

    @staticmethod
    def _create_order(order: list[tuple[str] | str] = None) -> str | None:
        if not order:
            return None
        answer = []
        for elem in order:
            if isinstance(elem, tuple):
                answer.append(f"{elem[0]},{elem[1]}")
            else:
                answer.append(f"{elem}")
        return ";".join(answer)

    @staticmethod
    def _create_filter(filters: tuple[str] = None) -> str | None:
        return ";".join(filters) if filters else None

    def get_collection(self, name: str, entity: Type[T],
                       order: list[tuple[str] | str] = None,
                       filter: tuple[str] = None,
                       search: str = None) -> CollectionAnswer:
        # TODO: реализовать листание
        answer_raw = self.requester.get(f'entity/{name}',
                                        params={
                                            'order': self._create_order(order),
                                            'filter': self._create_filter(filter),
                                            'search': search
                                        })
        answer = CollectionAnswer(answer_raw['context'], MetaArray.from_dict(answer_raw['meta']),
                                  [entity.from_dict(row) for row in answer_raw['rows']])
        return answer

    def get_entity(self, name: str, entity: Type[T], uuid: UUID) -> T:
        return entity.from_dict(self.requester.get(f'entity/{name}/{str(uuid)}'))

    def delete_entity(self, name: str, uuid: UUID) -> None:
        self.requester.delete(f'entity/{name}/{str(uuid)}')

    def create_entity(self, name: str, entity: T) -> T:
        return entity.__class__.from_dict(self.requester.post(f'entity/{name}',
                                                              entity.to_dict(omit_none=True)))

    def edit_entity(self, name, entity: T, uuid: UUID) -> T:
        return entity.__class__.from_dict(self.requester.put(f'entity/{name}/{str(uuid)}',
                                                             entity.to_dict(omit_none=True)))

    def mass_delete_entity(self, name: str, metas: list[Meta]) -> list[dict]:
        return self.requester.post(f'entity/{name}/delete',
                                   data=[{'meta': meta.to_dict(omit_none=True)} for meta in metas])

    def mass_create_entity(self, name: str, entities: list[T]) -> list[T]:
        raw_answer = self.requester.post(f'entity/{name}',
                                         [entity.to_dict(omit_none=True) for entity in entities])
        answer = []
        for raw_entity in raw_answer:
            answer.append(entities[0].__class__.from_dict(raw_entity))
        return answer
