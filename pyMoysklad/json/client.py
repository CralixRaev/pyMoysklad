from pyMoysklad.json.entity.country import Country
from pyMoysklad.json.requester import Requester


class JSONApi:
    def __init__(self, auth: str | tuple[str, str]):
        self.requester = Requester(auth)

    def list_countries(self) -> list[Country]:
        answer = self.requester.get("entity/country")
        return [Country.from_dict(country) for country in answer['rows']]