from enum import Enum


class GlobalErrorMassages(Enum):
    WRONG_STATUS_CODE = 'Received status code in not equal to expected'
    WRONG_COUNT_OF_ELEMENT = 'Received number of items is not equal to expected'

class UserErrors(Enum):
    WRONG_EMAIL = 'Email invalid'

