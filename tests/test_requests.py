import requests
import json


from configuration import USERS_URL
from src.base_class.response import Response
from src.pydantic_schemas.user import User


def test_get_users():
    r = requests.get(USERS_URL)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(User)

