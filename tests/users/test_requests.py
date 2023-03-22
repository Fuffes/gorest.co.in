import pytest
import requests
import json

from configuration import USERS_URL
from src.base_class.response import Response
from src.pydantic_schemas.user import User


def test_get_users(get_users):
    Response(get_users).assert_status_code(100).validate(User)


@pytest.mark.skip('not to be tested')
def test_another():
    assert 1 == 1


# pytest -s -v -k dev
# pytest -s -v -k "not dev"
# pytest -s -v --durations=3 -vv


@pytest.mark.dev
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1)
])
def test_calcc(first_value, second_value, result, calc):
    assert calc(first_value, second_value) == result


def test_another2(calc):
    print(calc(1, 2))


def test_failed():
    assert 1 == 2

