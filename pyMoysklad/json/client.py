from pyMoysklad.json.entity.country import Country, CountryMixin
from pyMoysklad.json.entity.region import RegionMixin
from pyMoysklad.json.requester import Requester


class JSONApi(CountryMixin,
              RegionMixin):
    def __init__(self, auth: str | tuple[str, str]):
        self.requester = Requester(auth)
