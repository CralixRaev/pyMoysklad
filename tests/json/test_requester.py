import pytest

from pyMoysklad.json.exceptions import AuthError
from pyMoysklad.json.requester import Requester


class TestRequester:
    def test_wrong_auth_login_password(self):
        with pytest.raises(AuthError):
            req = Requester(("totally wrong login", "and maybe not wrong password"))
            req.get("entity/country")

    def test_wrong_auth_token(self):
        with pytest.raises(AuthError):
            req = Requester("totally wrong token")
            req.get("entity/country")
