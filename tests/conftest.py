import pytest
import requests

from configuration import USERS_URL
from src.generator.player import Player


@pytest.fixture(scope='function')
def get_users():
    return requests.get(USERS_URL)


def _calc(a,b):
    return a+b

@pytest.fixture()
def calc():
    return _calc


@pytest.fixture
def get_player_generator():
    return Player()