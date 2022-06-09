import functools
import json
import logging
from urllib.parse import urljoin

import requests
from pyrate_limiter import Limiter, RequestRate, Duration
from requests.auth import HTTPBasicAuth
from requests_ratelimiter import LimiterSession

from pyMoysklad.json.exceptions import AuthError, ApiError, ERRORS

ENDPOINT = "https://online.moysklad.ru/api/remap/1.2/"


class TokenAuth(requests.auth.AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


class Requester:
    @staticmethod
    def _check_for_errors(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            answer = func(self, *args, **kwargs)
            if 'errors' in answer:
                error = answer['errors'][0]
                if error['code'] in ERRORS:
                    raise ERRORS[error['code']](error['error'])
                else:
                    exception = ApiError(error['error'], code=error['code'])
                    raise exception
            return answer

        return wrap

    @_check_for_errors
    def get(self, url: str, params: dict = None):
        self.session.auth = self._auth
        return self.session.get(urljoin(ENDPOINT, url), params=params).json()

    @_check_for_errors
    def post(self, url: str, data: dict):
        self.session.auth = self._auth
        return self.session.post(urljoin(ENDPOINT, url),
                                 data=json.dumps(data),
                                 headers={
                                     'content-type': 'application/json'
                                 }).json()

    @_check_for_errors
    def put(self, url: str, data: dict):
        self.session.auth = self._auth
        return self.session.put(urljoin(ENDPOINT, url), data=json.dumps(data)).json()

    @_check_for_errors
    def delete(self, url: str):
        self.session.auth = self._auth
        return self.session.delete(urljoin(ENDPOINT, url)).json()

    def __init__(self, auth: str | tuple[str, str]):
        self._auth: HTTPBasicAuth | TokenAuth
        if isinstance(auth, tuple):
            self._auth = HTTPBasicAuth(*auth)
        else:
            self._auth = TokenAuth(auth)
        self.session = LimiterSession(auth=self._auth,
                                      limiter=Limiter(RequestRate(45, Duration.SECOND * 3)))
