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
        self.requester = Requester(auth)

    def _get_collection(self, url: str, entity: abc.Object) -> CollectionAnswer:
        # TODO: реализовать листание
        answer_raw = self.requester.get(url)
        answer = CollectionAnswer(answer_raw['context'], MetaArray.from_dict(answer_raw['meta']),
                                  [entity.from_dict(row) for row in answer_raw['rows']])
        return answer
