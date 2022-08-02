import os

import pytest
import dotenv

from pymoysklad.json.client import JSONApi

dotenv.load_dotenv()


@pytest.fixture
def login():
    return os.getenv("LOGIN")


@pytest.fixture
def password():
    return os.getenv("PASSWORD")


@pytest.fixture(scope="package", autouse=True)
def client(login, password):
    return JSONApi((login, password))
