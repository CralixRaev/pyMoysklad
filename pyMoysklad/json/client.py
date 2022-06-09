from typing import Type
from urllib.parse import urljoin
from uuid import UUID

from pyMoysklad.json.entity import abc
from pyMoysklad.json.entity.country import Country, CountryMixin
from pyMoysklad.json.entity.region import RegionMixin
from pyMoysklad.json.entity.subscription import SubscriptionMixin
from pyMoysklad.json.meta import MetaArray
from pyMoysklad.json.requester import Requester
from pyMoysklad.json.utils.types import CollectionAnswer


class JSONApi(CountryMixin,
              RegionMixin,
              SubscriptionMixin):
    def __init__(self, auth: str | tuple[str, str]):
        self.requester: Requester = Requester(auth)

    def _create_order(self, order: list[tuple[str] | str] = None) -> str | None:
        if not order:
            return None
        answer = []
        for elem in order:
            if isinstance(elem, tuple):
                answer.append(f"{elem[0]},{elem[1]}")
            else:
                answer.append(f"{elem}")
        return ";".join(answer)

    def _create_filter(self, filters: tuple[str] = None) -> str | None:
        return ";".join(filters) if filters else None

    def _get_collection(self, url: str, entity: Type[abc.Object],
                        order: list[tuple[str] | str] = None,
                        filter: tuple[str] = None,
                        search: str = None) -> CollectionAnswer:
        # TODO: реализовать листание
        answer_raw = self.requester.get(url,
                                        params={
                                            'order': self._create_order(order),
                                            'filter': self._create_filter(filter),
                                            'search': search
                                        })
        answer = CollectionAnswer(answer_raw['context'], MetaArray.from_dict(answer_raw['meta']),
                                  [entity.from_dict(row) for row in answer_raw['rows']])
        return answer

    def _get_entity(self, url: str, entity: Type[abc.Object], uuid: UUID) -> abc.Object:
        return entity.from_dict(self.requester.get(f'{url}/{str(uuid)}'))

    def _create_entity(self, url, entity: abc.Object) -> abc.Object:
        return entity.__class__.from_dict(self.requester.post(url, entity.to_dict(omit_none=True)))
