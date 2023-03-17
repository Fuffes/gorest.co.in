import datetime

from pydantic import BaseModel, validator, Field


class User(BaseModel):
    id: int
    user_id: int
    title: str
    due_on: datetime
    status: str
