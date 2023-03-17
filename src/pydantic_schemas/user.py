from pydantic import BaseModel,validator
from src.enums.user_enums import *
from src.enums.global_emuns import UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Status

    @validator('email')
    def check_emeil(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
