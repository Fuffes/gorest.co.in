import pytest
import requests

from configuration import USERS_URL


@pytest.fixture(scope='function')
def get_users():
    return requests.get(USERS_URL)


def _calc(a,b):
    return a+b

@pytest.fixture()
def calc():
    return _calc